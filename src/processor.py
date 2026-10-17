# processor.py
from typing import List

class DataProcessor:
    """
    Basic numeric data processing.

    Stores a dataset and computes simple statistics like mean and variance.

    Attributes
    ----------
    data : list of float
        Numeric values stored in the processor.
    """

    def __init__(self, data: List[float]):
        """
        Initialize with a dataset.

        Parameters
        ----------
        data : list of float
            Numeric values to be processed.

        Examples
        --------
        >>> processor = DataProcessor([1.0, 2.0, 3.0])
        >>> processor.data
        [1.0, 2.0, 3.0]
        """
        self.data = data

    def mean(self) -> float:
        """
        Compute the arithmetic mean of the dataset.

        Returns
        -------
        float
            Mean of the dataset.

        Raises
        ------
        ValueError
            If the dataset is empty.

        Examples
        --------
        >>> processor = DataProcessor([1.0, 2.0, 3.0])
        >>> processor.mean()
        2.0
        """
        if not self.data:
            raise ValueError("Data is empty.")
        return sum(self.data) / len(self.data)

    def variance(self) -> float:
        """
        Compute the population variance of the dataset.

        Returns
        -------
        float
            Variance of the dataset.

        Raises
        ------
        ValueError
            If the dataset is empty.

        Examples
        --------
        >>> processor = DataProcessor([1.0, 2.0, 3.0])
        >>> processor.variance()
        0.6666666666666666
        """

        if not self.data:
            raise ValueError("Data is empty.")
        m = self.mean()
        return sum((x - m) ** 2 for x in self.data) / len(self.data)
    
    def median(self):
        """
        Compute the median value of the dataset.
        
        Returns
        -------
        float
            Median value of the dataset.

        Raises
        ------
        ValueError
            If the dataset is empty.

        Examples
        --------
        >>> processor = DataProcessor([1.0, 2.0, 3.0])
        >>> processor.variance()
        2.0
        """
        if not self.data:
            raise ValueError("Data is empty.")
        self.data.sort()
        if len(self.data) % 2 == 0:
            mid = (self.data[len(self.data) // 2] + self.data[(len(self.data) // 2) - 1]) / 2
        else:
            mid = self.data[len(self.data) // 2]
        return mid
    
    if __name__ == "__main__":
        p = DataProcessor([1, 2, 3])
        help(p.mean)