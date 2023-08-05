// clang-format off
/*
 * SPDX-FileCopyrightText: Copyright (c) 2023-present NVIDIA CORPORATION & AFFILIATES.
 * All rights reserved.
 * SPDX-License-Identifier: BSD-3-Clause
 */
// clang-format on
#pragma once
#include <c10/macros/Export.h>

#include <kernel_cache.h>
#include <python_frontend/fusion_record.h>

#include <memory>
#include <mutex>

namespace nvfuser::python_frontend {

//! \struct UserSchedule
//! \brief A container to hold a scheduled Fusion IR as well as an executor
//! to contain the corresponding generated kernel.
struct UserSchedule {
  UserSchedule();

  //! Scheduled Fusion IR
  std::unique_ptr<Fusion> schedule;
  //! Generated kernel container
  std::unique_ptr<FusionExecutor> executor;
};

//! \struct FusionSchedules
//! \brief A container for auto generated and user defined schedules
//! that correspond to compiled kernels for each complete Fusion Definition.
struct FusionSchedules {
  FusionSchedules();
  Fusion* preschedFusion();

  //! Schedules Automatically generated by nvFuser for dynamic inputs. (default)
  //! NOTE: The FusionExecutorCache also holds the Unscheduled Fusion IR
  std::unique_ptr<FusionExecutorCache> auto_gen_schedules;
  //! Schedules defined by the user for specific input sizes.
  //! They are also generated per device as all devices may not be the same.
  //! Key:   Input Encoding hash of Fusion inputs as is created by the
  //!        InputsIdLookup struct found inside of the FusionCache.
  //! Value: A vector based on device_id of User Defined Fusion Schedules.
  std::unordered_map<size_t, std::vector<UserSchedule>> user_def_schedules;
  //! Keeps a pointer to the last scheduled Fusion IR for printing
  Fusion* last_user_def_scheduled_ir;
  //! Keeps a pointer to the last executed executor for printing its cuda kernel
  FusionExecutor* last_user_def_executor;
  //! For thread-Safe locking of Fusion Schedules
  std::mutex scheds_lock;
};

//! \struct TrieNode
//! \brief Is the container for a Node in a prefix tree or trie
//! where each node represents a statement in a fusion definition and
//! the leaf Nodes represent a complete Fusion that is cached.

struct TORCH_CUDA_CU_API TrieNode {
  TrieNode(
      RecordFunctor* rec,
      TrieNode* _parent = nullptr,
      size_t _fusion_id = 0);

  // Queries whether the entry denotes a leaf node which also represents
  // a the end of Fusion entry in the cache.
  bool isTerminal() const;
  //! Serialize TrieNode using flatbuffers
  flatbuffers::Offset<serde::TrieNode> serialize(
      flatbuffers::FlatBufferBuilder& builder,
      const std::map<RecordFunctor*, size_t>&
          map_record_functor_to_trie_node_id);

  //! An entry's primary data is the record it holds
  std::unique_ptr<RecordFunctor> record;
  //! A hash map of the children for the current node.
  //! The hash map hashes a pointer to a RecordFunctor because
  //! the hash function is virtual.
  std::unordered_map<RecordFunctor*, std::unique_ptr<TrieNode>> children;
  //! An index into FusionCache's vector of nvFuser object that holds an
  //! unscheduled Fusion.  The id is only valid if the entry is terminal.
  size_t fusion_id;
  //! Count of times the Entry is traversed
  size_t visits;
  //! Parent node for printing
  TrieNode* parent;
  //! For thread-Safe locking of a node
  std::mutex trie_node_lock;
};

//! \class FusionCache
//! \brief A singleton class used in the nvFuser python interface
//! to manage the caching of fusions.
//!
//! The fusion cache implements a prefix tree (trie) of records in order to
//! cache fusions.  A leaf of the tree with a terminal node contains a
//! container for caching the kernels generated for specific fusions.
//!
//! \todo
//! Add the ability to evict a fusion.  There is currently a max number
//! of fusions that is checked to prevent a runaway case.
//!
//! \note
//! Thread-Safety is assured by the Python GIL.  If a no-GIL python is used
//! then further scrutiny needs to be applied to the mutexes used to limit
//! acccess to the singleton pointer, node creation, and user schedule
//! creation.  Otherwise, the Python GIL provides a natural thread based mutex
//! that does not allow for multiple threads to interact.

class TORCH_CUDA_CU_API FusionCache {
  //! The constructor is private given the FusionCache is only constructed
  //! as a singleton.
  FusionCache(size_t max_fusions);

  //! Copy and Assignment of the FusionCache is not supported
  FusionCache(const FusionCache&) = delete;
  FusionCache& operator=(const FusionCache&) = delete;

 public:
  //! The next 4 pubic methods are the python interface methods

  //! Gets a pointer to the singleton and creates a new one if necessary
  static FusionCache* get(size_t max_fusions = 8192);
  //! Number of fusions cached
  size_t numFusions() const;
  //! print cache contents
  void print(std::ostream& os) const;
  //! print cache stats
  void stats(std::ostream& os) const;
  //! Reset Cache to an empty state
  static void reset();
  //! Serialize Fusion Cache using flatbuffers
  void serialize(std::string filename) const;
  //! Deserialize Fusion Cache using flatbuffers
  void deserialize(std::string filename);

  //! The rest of the public methods are only used in C++

  //! Thread-Unsafe: Queries the current trie node to see if a record matches
  //! one of its children
  c10::optional<TrieNode*> queryChildren(TrieNode* node, RecordFunctor* rec)
      const;
  //! Query a Fusion's Schedules based on fusion id or cache id
  FusionSchedules* queryFusionSchedules(size_t fusion_id) const;
  //! Lookup the User Schedule Id and return null if one does not exist.
  //! NOTE: this method cannot be const because the InputsIdLookup can
  //! cause a modification to that data member for cache eviction.
  c10::optional<size_t> queryUserScheduleId(
      const FusionSchedules* scheds,
      const at::ArrayRef<c10::IValue>& inputs);
  //! Lookup the User Schedule based on Id
  const UserSchedule& queryUserSchedule(
      const FusionSchedules* scheds,
      size_t id,
      int device) const;
  //! Thread-Safe: Creates a child node for the current cache entry and an
  //! optional fusion_id is returned if the new entry is terminal
  TrieNode* createChild(TrieNode* node, RecordFunctor* rec);
  //! Lookup the User Schedule based on Id
  UserSchedule* createUserSchedule(
      FusionSchedules* scheds,
      const at::ArrayRef<c10::IValue>& inputs,
      int device);
  //! Get the root Trie ptr
  TrieNode* rootTriePtr();

 private:
  //! The static pointer to the FusionCache
  static FusionCache* singleton_;
  //! Lock for accessing the singleton by multiple threads
  static std::mutex singleton_lock_;

  //! The max allowed number of fusions in the cache
  size_t max_fusions_;
  //! The root (start) of the prefix tree to start a cache look up of a given
  //! fusion definition.
  std::unique_ptr<TrieNode> root_;
  //! A vector of nvFuser Fusion IR fusions.
  std::vector<std::unique_ptr<FusionSchedules>> fusions_;
  //! A vector of Terminal trie nodes for Stats collection
  std::vector<TrieNode*> terminal_nodes_;

  //! Items specifically to aid user defined schedules these data members
  //! are for the mechanics of user schedule usage and don't make sense as
  //! part of an abstraction

  // Inputs for user defined schedules are encoded into an integer Id
  // NOTE: I would prefer this be per FusionSchedules object but the container
  // is not allowed to be copied or moved.
  InputsIdLookup user_def_input_encodings_;
};

} // namespace nvfuser::python_frontend
