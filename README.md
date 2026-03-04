# LRU Cache (From Scratch) + Workload Simulator (Python)

An **LRU (Least Recently Used) cache** evicts the item that hasn’t been accessed for the longest time when the cache reaches its capacity.  
This project implements an LRU cache **from scratch** in Python and simulates it on a workload of `GET` / `PUT` operations.

## Features

- ✅ **LRU Cache** with `get(key)` and `put(key, value)`
- ✅ **O(1)** average-time operations using:
  - **Custom HashMap** (no built-in `dict`)
  - **Custom Doubly Linked List** (move-to-front + tail eviction)
- ✅ Configurable **capacity**
- ✅ Workload simulation from a file (sequence of `GET` / `PUT`)
- ✅ Simulation report:
  - total gets, hits, misses, hit rate (%)
  - final cache contents (MRU → LRU)
- ✅ Edge cases covered:
  - capacity = 1
  - all gets on empty cache
  - repeated puts with same key (update + move to MRU)
- ✅ Correctness verification via tests + manual trace

## Data Structures

**HashMap:** `key -> node reference` for O(1) lookup  
**Doubly Linked List:** keeps usage order  
- **Head** = MRU (most recently used)  
- **Tail** = LRU (least recently used)

On every `get` / `put`, the key becomes **MRU** (moved to head).  
On overflow, the cache evicts **LRU** (tail node).

## Complexity

- `get(key)` → **O(1)** average
- `put(key, value)` → **O(1)** average

Each operation does a constant number of pointer updates in the DLL and constant-time average lookup/update in the custom HashMap.

## Project Structure
