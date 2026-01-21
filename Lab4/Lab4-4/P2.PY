from abc import ABC, abstractmethod


class Vehicle(ABC):
    """
    Abstract base class representing a general vehicle.

    Attributes:
        make (str): Manufacturer of the vehicle.
        model (str): Model name.
        year (int): Manufacturing year.
        is_running (bool): Engine running state.
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Initializes a Vehicle object.

        Args:
            make (str): Vehicle manufacturer.
            model (str): Vehicle model.
            year (int): Manufacturing year.

        Raises:
            ValueError: If input values are invalid.
        """
        if not isinstance(make, str) or not make:
            raise ValueError("make must be a non-empty string")
        if not isinstance(model, str) or not model:
            raise ValueError("model must be a non-empty string")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("year must be a positive integer")

        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    @abstractmethod
    def start_engine(self):
        """
        Starts the vehicle engine.

        Returns:
            str: Status message.
        """
        pass

    @abstractmethod
    def stop_engine(self):
        """
        Stops the vehicle engine.

        Returns:
            str: Status message.
        """
        pass

    def get_info(self):
        """
        Returns basic vehicle information.

        Returns:
            str: Vehicle description string.
        """
        return f"{self.year} {self.make} {self.model}"


class CommercialVehicle:
    """
    Represents a commercial vehicle capable of carrying cargo.

    Attributes:
        license_number (str): Vehicle registration number.
        max_load (float): Maximum allowed cargo weight.
        current_load (float): Current cargo weight.
    """

    def __init__(self, license_number: str, max_load: float):
        """
        Initializes a CommercialVehicle object.

        Args:
            license_number (str): Registration number.
            max_load (float): Maximum cargo load.

        Raises:
            ValueError: If inputs are invalid.
        """
        if not isinstance(license_number, str) or not license_number:
            raise ValueError("license_number must be a non-empty string")
        if not isinstance(max_load, (int, float)) or max_load <= 0:
            raise ValueError("max_load must be a positive number")

        self.license_number = license_number
        self.max_load = float(max_load)
        self.current_load = 0.0

    def load_cargo(self, weight: float):
        """
        Attempts to load cargo.

        Args:
            weight (float): Cargo weight.

        Returns:
            bool: True if cargo loaded successfully, otherwise False.
        """
        if not isinstance(weight, (int, float)) or weight <= 0:
            return False

        if self.current_load + weight <= self.max_load:
            self.current_load += weight
            return True
        return False

    def unload_cargo(self, weight: float):
        """
        Removes cargo from the vehicle.

        Args:
            weight (float): Weight to remove.

        Returns:
            float: Remaining current load.
        """
        if not isinstance(weight, (int, float)) or weight <= 0:
            return self.current_load

        if weight <= self.current_load:
            self.current_load -= weight
        else:
            self.current_load = 0

        return self.current_load


class Car(Vehicle):
    """
    Represents a passenger car.

    Attributes:
        num_doors (int): Number of doors.
    """

    def __init__(self, make, model, year, num_doors):
        """
        Initializes a Car object.

        Args:
            make (str): Manufacturer.
            model (str): Model.
            year (int): Manufacturing year.
            num_doors (int): Number of doors.

        Raises:
            ValueError: If num_doors is invalid.
        """
        super().__init__(make, model, year)

        if not isinstance(num_doors, int) or num_doors <= 0:
            raise ValueError("num_doors must be a positive integer")

        self.num_doors = num_doors

    def start_engine(self):
        """
        Starts the car engine.

        Returns:
            str: Engine start message.
        """
        self.is_running = True
        return "Car engine started."

    def stop_engine(self):
        """
        Stops the car engine.

        Returns:
            str: Engine stop message.
        """
        self.is_running = False
        return "Car engine stopped."


class Trailer(CommercialVehicle):
    """
    Represents a cargo trailer.

    Attributes:
        num_axles (int): Number of axles.
    """

    def __init__(self, license_number, max_load, num_axles=2):
        """
        Initializes a Trailer object.

        Args:
            license_number (str): Registration number.
            max_load (float): Maximum load.
            num_axles (int, optional): Number of axles. Defaults to 2.
        """
        super().__init__(license_number, max_load)

        if not isinstance(num_axles, int) or num_axles <= 0:
            raise ValueError("num_axles must be positive")

        self.num_axles = num_axles

    def get_weight_per_axle(self):
        """
        Calculates load per axle.

        Returns:
            float: Load divided by number of axles.
        """
        return self.current_load / self.num_axles if self.num_axles else 0


class DeliveryVan(Car, CommercialVehicle):
    """
    Represents a delivery van using multiple inheritance.

    Attributes:
        delivery_mode (bool): Indicates delivery operation status.
    """

    def __init__(self, make, model, year, num_doors, license_number, max_load):
        """
        Initializes a DeliveryVan object.
        """
        Car.__init__(self, make, model, year, num_doors)
        CommercialVehicle.__init__(self, license_number, max_load)

        self.delivery_mode = False

    def toggle_delivery_mode(self):
        """
        Toggles delivery mode.

        Returns:
            str: Delivery mode status message.
        """
        self.delivery_mode = not self.delivery_mode
        return f"Delivery mode is now {'ON' if self.delivery_mode else 'OFF'}."

    def get_info(self):
        """
        Returns extended van information.

        Returns:
            str: Full van description.
        """
        return (
            f"{super().get_info()} | Doors: {self.num_doors} | "
            f"License: {self.license_number} | "
            f"Load: {self.current_load}/{self.max_load}"
        )

    def begin_service(self):
        """
        Executes a full delivery service cycle.
        """
        print(self.get_info())

        print("Load success:", self.load_cargo(50))
        print(self.start_engine())
        print(self.toggle_delivery_mode())
        print(self.stop_engine())
        print("Remaining load:", self.unload_cargo(50))
        print(self.toggle_delivery_mode())


if __name__ == "__main__":
    van = DeliveryVan("Ford", "Transit", 2024, 4, "DV-1001", 500)
    van.begin_service()
