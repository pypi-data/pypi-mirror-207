class Zeros:

    @staticmethod
    def zeros(p: int) -> int:
        """
        Returns the number of trailing zeros in the binary representation of p.

        Parameters
        ----------
        p: int
            Input integer.

        Returns
        -------
        int
            Number of trailing zeros in the binary representation of p.
        """
        count = 0
        while p % 2 == 0 and p > 0:
            count += 1
            p = p // 2
        return count