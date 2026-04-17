Aaditya Raj Soni
URN - 2024-B-26092004
1. Problem Statement (Window Manager) - Build a simple desktop-style window
manager. Each window has a unique ID and can be in one of three states:
OPEN, MINIMIZED, or CLOSED. Open windows must be maintained in a strict
z-order from top to bottom. Support the following operations: open a window (or
bring it to the top if it already exists), focus a window (bringing it to the top,
restoring if minimized), minimize, restore, and close a window, along with queries
to get the top-most window and list all open windows from top to bottom.
2. Data structure selection - Used dict for state and OrderedDict as the z-order
stack (hashmap + doubly linked list internally), giving O(1) for all core operations.
3. Edge Cases Handled- Unknown/closed IDs treated as no-ops, empty top()
returns -1, reopening a closed ID creates a fresh window, double-minimize and
restore-on-open are safely ignored.
4. Assumptions: FOCUS on unknown/closed IDs is a no-op (not auto-created,
since that's OPEN's job); RESTORE only acts on minimized windows
