from abc import ABC, abstractmethod


class IDisplayable(ABC):
    """
    Interface for objects that can display their data as a formatted string.
    Following the Interface Segregation Principle (ISP).
    """

    @abstractmethod
    def display(self) -> str:
        """
        Returns a formatted string representation of the object's data.

        Returns:
            str: Formatted display string
        """
        pass