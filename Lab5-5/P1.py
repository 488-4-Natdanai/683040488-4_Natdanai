import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
    QLabel, QLineEdit, QDateEdit, QSpinBox,
    QPushButton, QDialog, QMessageBox, QScrollArea,
    QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, Signal, QDate
from PySide6.QtGui import QFont

class RoomCard(QWidget):
    """
    Room information card — Custom Widget Class
    Practice:
      - Inheriting QWidget
      - Signal to pass data to parent
      - select() / deselect() methods to change visual state
    """

    # Signal: emits (room_name, price) when user clicks Select
    room_selected = Signal(str, int)

    def __init__(self, room_name: str, price: int, description: str, emoji: str = "🏨"):
        super().__init__()
        self._is_selected = False
        self.room_name = room_name
        self.price = price

        self._build_ui(emoji, description)
        self.deselect()  # Set default style

    def _build_ui(self, emoji: str, description: str):
        self.setFixedSize(200, 200)
        self.setCursor(Qt.PointingHandCursor)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(6)

        # Create labels and button in the card

        self.emoji = QLabel(emoji)
        self.emoji.setAlignment(Qt.AlignCenter)
        self.emoji.setStyleSheet("font-size: 40px;")
        

        self.name = QLabel(self.room_name)
        self.name.setAlignment(Qt.AlignCenter)
        self.name.setStyleSheet("""
            font-size: 14px;
            font-weight: 700;
            color: #111827;
        """)
        
        self.price_label = QLabel(f"{self.price} / night")
        self.price_label.setAlignment(Qt.AlignCenter)
        self.price_label.setStyleSheet("""
            font-size: 12px;
            color: #1f1f1f;
        """)

        self.des = QLabel(description)
        self.des.setAlignment(Qt.AlignCenter)
        self.des.setWordWrap(True)
        self.des.setStyleSheet("""
            font-size: 11px;
            color: #9ca3af;
        """)

        self.select_btn = QPushButton("Select Room")
        self.select_btn.clicked.connect(self.is_selected)

        # Add labels and button to the layout
        layout.addWidget(self.emoji)
        layout.setSpacing(5)
        layout.addWidget(self.name)
        layout.setSpacing(1)
        layout.addWidget(self.price_label)
        layout.addWidget(self.des)
        layout.addWidget(self.select_btn)

    def _on_select_clicked(self):
        """When button is clicked, emit signal to notify parent"""
        self.room_selected.emit(self.name.text(),self.price)

    # Appearance and state when the button is selected
    def select(self):
        """Change to selected state (green border)"""
        self._is_selected = True

        self.setStyleSheet("""
            RoomCard {
                background-color: #f0fdf4;
                border: 2px solid #22c55e;
                border-radius: 12px;
            }
        """)
        self.select_btn.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 5px;
                font-weight: bold;
            }
        """)
        self.select_btn.setText("✓ Selected")

    def deselect(self):
        """Change back to normal state"""
        self._is_selected = False

        self.setStyleSheet("""
            RoomCard {
                background-color: #ffffff;
                border: 2px solid #e5e7eb;
                border-radius: 12px;
            }
            RoomCard:hover {
                border: 2px solid #6366f1;
                background-color: #f5f3ff;
            }
        """)
        self.select_btn.setStyleSheet("""
            QPushButton {
                background-color: #6366f1;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 5px;
            }
            QPushButton:hover { background-color: #4f46e5; }
        """)
        self.select_btn.setText("Select Room")

    def is_selected(self):
        if not self._is_selected:
            self.select()
        self._on_select_clicked()
    
class ConfirmDialog(QDialog):
    """
    Booking confirmation popup — Custom Dialog Class
    Practice:
      - Inheriting QDialog
      - Building layout and widgets inside the dialog manually
    """

    def __init__(self, guest_name: str, room_name: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Booking Confirmed")
        self.setFixedSize(360, 220)
        self.setModal(True)
        self._build_ui(guest_name, room_name)

    def _build_ui(self, guest_name: str, room_name: str):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(12)

        # Create labels and button in the card
        self.check = QLabel("✅") 
        self.check.setAlignment(Qt.AlignCenter)
        self.check.setStyleSheet("font-size: 40px;")

        self.success = QLabel("Booking Successful!")
        self.success.setAlignment(Qt.AlignCenter)
        self.success.setStyleSheet("""
            font-size: 14px;
            font-weight: 700;
            color: #22c55e;
        """)
        self.des = QLabel(f"Dear {guest_name},\n{room_name} is ready to welcome you!🎊")
        self.des.setAlignment(Qt.AlignCenter)
        self.des.setWordWrap(True)
        self.des.setStyleSheet("""
            font-size: 11px;
            color: #9ca3af;
        """)

        self.ok = QPushButton("OK")
        self.ok.setFixedHeight(30)
        self.ok.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0 28px;
            }
            QPushButton:hover { background-color: #199245; }
        """)
        # Add labels and button to the layout
        layout.addWidget(self.check)
        layout.addWidget(self.success)
        layout.addWidget(self.des)
        layout.addWidget(self.ok)

# ─────────────────────────────────────────────
#  Page 1: Booking Page
# ─────────────────────────────────────────────
class BookingPage(QWidget):
    """
    Page 1 — Guest information form and room selection
    """

    def __init__(self):
        super().__init__()
        self.selected_room = None
        self.selected_price = 0
        self.cards = [] # a list of RoomCard object
        self._build_ui()

    def _build_ui(self):
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)

        container = QWidget()
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(30, 24, 30, 24)
        main_layout.setSpacing(20)
        # Add widgets to the main_layout

        # Title
        title = QLabel("🏨 Book Your Stay at CozyStay")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color: #1e1b4b;")
        main_layout.addWidget(title)

        subtitle = QLabel("Fill in your details and choose your room")
        subtitle.setFont(QFont("Segoe UI", 10))
        subtitle.setStyleSheet("color: #6b7280;")
        main_layout.addWidget(subtitle)

        # ── Section 1: Guest Info Form ──
        form_title = QLabel("📋 Guest Information")
        form_title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        form_title.setStyleSheet("color: #374151; margin-top: 8px;")
        main_layout.addWidget(form_title)

        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background-color: #f9fafb;
                border-radius: 10px;
            }
        """)
        form_layout = QFormLayout()
        form_layout.setLabelAlignment(Qt.AlignRight)
        form_layout.setContentsMargins(20, 20, 20, 20)
        form_frame.setLayout(form_layout)

        # Create widgets for inputs
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.checkin_input = QDateEdit()
        self.checkin_input.setCalendarPopup(True)
        self.checkin_input.setDisplayFormat("M/dd/yy")
        self.checkin_input.setDate(QDate.currentDate())
        self.checkout_input = QDateEdit()
        self.checkout_input.setCalendarPopup(True)
        self.checkout_input.setDisplayFormat("M/dd/yy")
        self.checkout_input.setDate(QDate.currentDate().addDays(1))
        self.guests_input = QSpinBox()
        self.guests_input.setRange(1,10)
        self.guests_input.setValue(1)
        self.guests_input.setSuffix(" guest(s)")

        # Set style for inputs and their labels
        input_style = """
            QLineEdit, QDateEdit, QSpinBox {
                border: 1px solid #d1d5db;
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 13px;
                background: white;
            }
            QLineEdit:focus, QDateEdit:focus, QSpinBox:focus {
                border: 1px solid #6366f1;
            }
        """
        for w in [self.name_input, self.phone_input,
                  self.checkin_input, self.checkout_input, self.guests_input]:
            w.setStyleSheet(input_style)
            w.setMinimumWidth(200)

        label_style = "font-size: 13px; color: #374151; font-weight: bold;"
        for text, widget in [
            ("Full Name :",       self.name_input),
            ("Phone Number :",    self.phone_input),
            ("Check-in Date :",   self.checkin_input),
            ("Check-out Date :",  self.checkout_input),
            ("Guests :",          self.guests_input)]:
            lbl = QLabel(text)
            lbl.setStyleSheet(label_style)
            
            # add label and widget to your layout
            form_layout.addRow(lbl, widget)
        main_layout.addWidget(form_frame)
            

        # ── Section 2: Room Selection ──
        room_title = QLabel("🛏 Select a Room")
        room_title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        room_title.setStyleSheet("color: #374151; margin-top: 8px;")
        main_layout.addWidget(room_title)

        rooms_data = [
            ("Standard Room", 50,  "Single bed, Free Wi-Fi",             "🛏"),
            ("Deluxe Room",   120, "Double bed, Ocean view, Wi-Fi",      "🌊"),
            ("Suite Room",    250, "Living room, Jacuzzi, Premium view", "👑"),
            ("Family Room",   160, "2 Bedrooms, Perfect for families",   "👨‍👩‍👧‍👦"),
        ]

        
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(14)
        cards_layout.setContentsMargins(0, 0, 0, 0)

        # Create cards according to the info above
        for name, price, desc, emoji in rooms_data:
            card = RoomCard(name, price, desc, emoji)
            cards_layout.addWidget(card)
        # Remember to put each card in self.cards
            self.cards.append(card)
        # also catch the emitted signal from each card
            card.room_selected.connect(self._on_room_selected)
        

        cards_layout.addStretch()
        main_layout.addLayout(cards_layout)


        # ── Buttons ──
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)

        self.clear_btn = QPushButton("🗑  Clear Info")
        self.clear_btn.setFixedHeight(42)
        self.clear_btn.setFont(QFont("Segoe UI", 11))
        self.clear_btn.setCursor(Qt.PointingHandCursor)
        self.clear_btn.clicked.connect(self.clear_form)
        self.clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #f3f4f6;
                color: #374151;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                padding: 0 20px;
            }
            QPushButton:hover { background-color: #e5e7eb; }
        """)
        # Connect the button's signal to a slot

        self.next_btn = QPushButton("Next  →")
        self.next_btn.setFixedHeight(42)
        self.next_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.next_btn.setCursor(Qt.PointingHandCursor)
        self.next_btn.clicked.connect(self.get_booking_data)
        self.next_btn.setStyleSheet("""
            QPushButton {
                background-color: #6366f1;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0 28px;
            }
            QPushButton:hover { background-color: #4f46e5; }
        """)

        btn_layout.addWidget(self.clear_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.next_btn)

        main_layout.addLayout(btn_layout)
        main_layout.addStretch()

        scroll.setWidget(container)

        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)

    def _on_room_selected(self, room_name: str, price: int):
        """Receive signal from RoomCard, update state, deselect other cards"""
        for card in self.cards:
            if card.room_name != room_name:
                card.deselect()
        self.selected_room = room_name
        self.selected_price = price


    def clear_form(self):
        """Clear all form fields and deselect all room cards"""

        # Clear text fields
        self.name_input.clear()
        self.phone_input.clear()

        # Reset dates
        self.checkin_input.setDate(QDate.currentDate())
        self.checkout_input.setDate(QDate.currentDate().addDays(1))

        # Reset guests
        self.guests_input.setValue(1)

        # Deselect all room cards
        for card in self.cards:
            card.deselect()

        # Reset selected room data
        self.selected_room = None
        self.selected_price = 0

    def get_booking_data(self):
        """Collect form data — returns None if validation fails"""
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        checkin = self.checkin_input.date()
        checkout = self.checkout_input.date()
        guests = self.guests_input.value()

        if not name:
            QMessageBox.warning(self, "Missing Information", "Please enter your full name.")
            return None
        if not phone:
            QMessageBox.warning(self, "Missing Information", "Please enter your phone number.")
            return None
        if checkin >= checkout:
            QMessageBox.warning(self, "Invalid Dates",
                                "Check-out date must be after check-in date.")
            return None
        if not self.selected_room:
            QMessageBox.warning(self, "No Room Selected",
                                "Please select a room before proceeding.")
            return None

        nights = checkin.daysTo(checkout)
        total = nights * self.selected_price

        # Create a dictionary of all values to be returned
        data_dict = {
        "room": self.selected_room,
        "price": self.selected_price,
        "name": name,
        "phone": phone,
        "checkin": checkin.toString("M/dd/yy"),
        "checkout": checkout.toString("M/dd/yy"),
        "nights": nights,
        "guests": guests,
        "total": total
        }
        return data_dict

# ─────────────────────────────────────────────
#  PAGE 2: ReviewPage
# ─────────────────────────────────────────────
class ReviewPage(QWidget):
    """
    Page 2 — Review booking details before submitting
    """

    def __init__(self):
        super().__init__()
        self.current_data = {}
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(16)

        title = QLabel("📋 Booking Summary")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color: #1e1b4b;")

        subtitle = QLabel("Please review your details before confirming")
        subtitle.setFont(QFont("Segoe UI", 10))
        subtitle.setStyleSheet("color: #6b7280;")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        self.info_frame = QFrame()
        self.info_frame.setStyleSheet("""
            QFrame {
                background-color: #f9fafb;
                border-radius: 12px;
            }
        """)

        # You can use other layout, like a form layout
        self.info_layout = QFormLayout(self.info_frame)

        display_data = [
            ("🛏  Room",            ""),
            ("💰  Price / Night",   f"$ -"),
            ("👤  Guest Name",      ""),
            ("📞  Phone",           ""),
            ("📅  Check-in",        ""),
            ("📅  Check-out",       ""),
            ("🌙  Nights",          f"- night(s)"),
            ("👥  Guests",          f"- guest(s)"),
        ]

        key_style = "font-weight: bold; color: #374151; font-size: 13px;"
        val_style = "color: #1f2937; font-size: 13px;"

        # Put labels and placeholder into the layout
        self.value_labels = {}

        for key, value in display_data:
            key_label = QLabel(key)
            key_label.setStyleSheet(key_style)

            value_label = QLabel(value)
            value_label.setStyleSheet(val_style)

            self.info_layout.addRow(key_label, value_label)
            self.value_labels[key] = value_label

        layout.addWidget(self.info_frame)

        # hline
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color: #e5e7eb;")
        layout.addWidget(line)

        # Create the Total label and add to the layout
        self.total_label = QLabel("Total: $ -")
        self.total_label.setAlignment(Qt.AlignRight)
        self.total_label.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #6366f1;
            margin-top: 10px;
        """)
        layout.addWidget(self.total_label)


        layout.addStretch()

        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)

        self.back_btn = QPushButton("←  Back")
        self.back_btn.setFixedHeight(44)
        self.back_btn.setFont(QFont("Segoe UI", 11))
        self.back_btn.setCursor(Qt.PointingHandCursor)
        self.back_btn.setStyleSheet("""
            QPushButton {
                background-color: #f3f4f6;
                color: #374151;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                padding: 0 22px;
            }
            QPushButton:hover { background-color: #e5e7eb; }
        """)

        self.submit_btn = QPushButton("✅  Confirm Booking")
        self.submit_btn.setFixedHeight(44)
        self.submit_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.submit_btn.setCursor(Qt.PointingHandCursor)
        self.submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0 28px;
            }
            QPushButton:hover { background-color: #16a34a; }
        """)

        btn_layout.addWidget(self.back_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.submit_btn)
        layout.addLayout(btn_layout)

    def load_data(self, data: dict):
        """Receive data dict from BookingPage and populate the review layout"""
        self.current_data = data    

        # Set all values from data in appropriate labels
        self.value_labels["🛏  Room"].setText(data["room"])
        self.value_labels["💰  Price / Night"].setText(f"$ {data['price']}")
        self.value_labels["👤  Guest Name"].setText(data["name"])
        self.value_labels["📞  Phone"].setText(data["phone"])
        self.value_labels["📅  Check-in"].setText(data["checkin"])
        self.value_labels["📅  Check-out"].setText(data["checkout"])
        self.value_labels["🌙  Nights"].setText(f"{data['nights']} night(s)")
        self.value_labels["👥  Guests"].setText(f"{data['guests']} guest(s)")

        self.total_label.setText(f"Total: $ {data['total']}")



class MainWindow(QMainWindow):
    """
    Main window — uses QStackedWidget to manage 2 pages
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CozyStay — Hotel Booking System")
        self.setMinimumSize(820, 680)
        self.resize(900, 720)

        # QStackedWidget as central widget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Create pages
        self.book = BookingPage()
        self.review = ReviewPage()

        # Add to stack: index 0 = booking, index 1 = review
        self.stack.addWidget(self.book)
        self.stack.addWidget(self.review)

        # Connect navigation

        # booking page: connect next_btn
        self.book.next_btn.clicked.connect(self._go_to_review)

        # review page: connect back_btn
        self.review.back_btn.clicked.connect(self._go_to_booking)

        # review page: connect submit_btn
        self.review.submit_btn.clicked.connect(self._on_submit)

        # Start on page 0
        # Set current stack index to the first page
        self.stack.setCurrentIndex(0)
        

        self.setStyleSheet("""
            QMainWindow { background-color: #f0f0ff; }
            QScrollArea  { background-color: transparent; }
            QWidget      { font-family: 'Segoe UI', 'Tahoma', sans-serif; }
        """)

    # Slot for the next_btn on the booking page
    def _go_to_review(self):
        """Validate form, then switch to Review page"""
        
        data = self.book.get_booking_data()

        if data is None:
            return
        
        # Load data into the review page
        self.review.load_data(data)
        
        # Set stack index to the review page
        self.stack.setCurrentIndex(1)


    # Slot for the back_btn on the review page
    def _go_to_booking(self):
        """Go back to Booking page, form data remains intact"""
        self.stack.setCurrentIndex(0)
        pass


    # slot for the submit_btn on the review page
    def _on_submit(self):
        """Show ConfirmDialog, then reset the entire app"""
        pass
        # Create a ConfirmDialog object
        # passing in the name and room
        # then show the dialog
        name = self.review.current_data["name"]
        room = self.review.current_data["room"]

        dialog = ConfirmDialog(name, room, self)
        dialog.ok.clicked.connect(dialog.accept)
        dialog.exec()

        # Clear booking page data
        self.book.clear_form()

        # Go back to booking page
        self.stack.setCurrentIndex(0)



def main():
    sys.argv += ['-platform', 'windows:darkmode=1']
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()