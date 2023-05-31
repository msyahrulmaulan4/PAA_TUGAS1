class Delivery:
    def __init__(self, delivery_number, status):
        self.delivery_number = delivery_number
        self.status = status

class DeliveryTracker:
    def __init__(self):
        self.delivery_table = {}

    def add_delivery(self, delivery):
        self.delivery_table[delivery.delivery_number] = delivery

    def track_delivery(self, delivery_number):
        if delivery_number in self.delivery_table:
            return self.delivery_table[delivery_number].status
        else:
            return "Delivery not found"

# Contoh penggunaan mekanisme pencarian cepat berdasarkan nomor pengiriman menggunakan tabel hash
tracker = DeliveryTracker()

delivery1 = Delivery("ABC123", "On the way")
delivery2 = Delivery("DEF456", "Delivered")
delivery3 = Delivery("GHI789", "In transit")

tracker.add_delivery(delivery1)
tracker.add_delivery(delivery2)
tracker.add_delivery(delivery3)

# Melacak status pengiriman berdasarkan nomor pengiriman
print(tracker.track_delivery("ABC123"))  # Output: On the way
print(tracker.track_delivery("DEF456"))  # Output: Delivered
print(tracker.track_delivery("XYZ999"))  # Output: Delivery not found

