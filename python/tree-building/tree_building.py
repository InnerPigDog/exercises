class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    # There has to be a root record
    if not records:
        return None

    # Sort records ascenting according to their ID
    records.sort(key=lambda x: x.record_id)

    # Intialize the root of the tree
    root = Node(0)

    # IDs have boundaries
    if not (records[0].record_id == 0) or len(records) != records[-1].record_id + 1:
        raise ValueError("Record id is invalid or out of order.")

    # Check if other records are valid
    for r in records:
        
        # Record ID and Parent ID are usually not the same.
        if r.record_id == r.parent_id and r.record_id != 0:
            raise ValueError("Only root should have equal record and parent id.")
        
        # Child records have a higher ID than there Parent record.
        if r.record_id < r.parent_id:
            raise ValueError("Node record_id should be smaller than it's parent_id.")
    
    # Build record tree
        # Add children to root
        if r.parent_id == 0 and r.record_id != 0:
            root.children.append(Node(r.record_id))
        
        # Or add grandchildren
        elif r.record_id != 0:
            for child in root.children:
                if child.node_id == r.parent_id:
                    child.children.append(Node(r.record_id))
                    break
    return root

        
        
        

        
        
