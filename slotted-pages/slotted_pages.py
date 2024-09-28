class SlottedPage:
    def __init__(self, page_size):
        self.page_size = page_size                    # Total size of the page
        self.page_header_size = 16                    # Reserve some space for the page header
        self.free_space_offset = self.page_size       # Points to where free space begins
        self.slots = []                               # List of (offset, length) for records
        self.data = bytearray(self.page_size)         # Bytearray to store the actual data
        self.records = {}                             # Store records in a dictionary

    def insert_record(self, record):
        """Insert a record into the page"""
        record_bytes = record.encode('utf-8')
        record_length = len(record_bytes)

        # Check if there's enough space to insert the record
        if self.free_space_offset - (self.page_header_size + len(self.slots) * 8) < record_length:
            raise ValueError("Not enough space in the page to insert the record")

        # Update free space offset
        self.free_space_offset -= record_length

        # Insert record into the page's data area
        self.data[self.free_space_offset:self.free_space_offset + record_length] = record_bytes

        # Add a slot pointing to the record
        self.slots.append((self.free_space_offset, record_length))
        self.records[len(self.slots) - 1] = record

        print(f"Record i nserted at offset {self.free_space_offset}, length {record_length}")

    def delete_record(self, slot_id):
        """Delete a record using the slot ID"""
        if slot_id >= len(self.slots) or self.slots[slot_id] is None:
            raise ValueError("Invalid slot ID")

        # Mark the slot as deleted
        self.slots[slot_id] = None
        del self.records[slot_id]
        print(f"Record at slot {slot_id} deleted")

    def compact_page(self):
        """Compact the page to remove deleted records and free up space"""
        compacted_data = bytearray(self.page_size)
        new_slots = []
        free_space_offset = self.page_size

        # Copy valid records into the new data array
        for slot in self.slots:
            if slot is not None:
                offset, length = slot
                free_space_offset -= length
                compacted_data[free_space_offset:free_space_offset + length] = self.data[offset:offset + length]
                new_slots.append((free_space_offset, length))

        # Update page with compacted data
        self.data = compacted_data
        self.slots = new_slots
        self.free_space_offset = free_space_offset
        print(f"Page compacted, free space starts at offset {self.free_space_offset}")

    def display_page(self):
        """Display the current state of the page"""
        print(f"Page Size: {self.page_size}")
        print(f"Free Space Offset: {self.free_space_offset}")
        print(f"Slots: {self.slots}")
        for i, (offset, length) in enumerate(self.slots):
            record_data = self.data[offset:offset + length].decode('utf-8')
            print(f"Slot {i}: Offset {offset}, Length {length}, Record '{record_data}'")

# Create a slotted page with a total size of 128 bytes
page = SlottedPage(page_size=128)

# Insert some records
page.insert_record("Record 1")
page.insert_record("Record 2")
page.insert_record("Record 3")

# Display the current state of the page
page.display_page()

# Delete a record (for example, the record at slot 1)
page.delete_record(1)

# Display the page after deletion
print("\nAfter Deletion:")
page.display_page()

# Compact the page to remove the gap created by the deleted record
page.compact_page()

# Display the page after compaction
print("\nAfter Compaction:")
page.display_page()
