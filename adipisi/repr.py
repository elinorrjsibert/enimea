def bubble_sort_signal(signal):
    """
    Sorts a signal using the bubble sort algorithm.

    Parameters:
    signal (list): The signal to be sorted.

    Returns:
    list: The sorted signal.
    """
    n = len(signal)
    for i in range(n):
        for j in range(0, n-i-1):
            if signal[j] > signal[j+1]:
                signal[j], signal[j+1] = signal[j+1], signal[j]
    return signal

# Example usage
signal = [64, 34, 25, 12, 22, 11, 90]
sorted_signal = bubble_sort_signal(signal)
print("Sorted signal using Bubble Sort:", sorted_signal)
