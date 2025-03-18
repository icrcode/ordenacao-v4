from .bubble_sort import BubbleSort
from .bubble_sort_melhorado import BubbleSortMelhorado
from .insertion_sort import InsertionSort
from .selection_sort import SelectionSort
from .quick_sort import QuickSort
from .merge_sort import MergeSort
from .tim_sort import TimSort

estrategias = {
    "Bubble Sort": BubbleSort(),
    "Bubble Sort Melhorado": BubbleSortMelhorado(),
    "Insertion Sort": InsertionSort(),
    "Selection Sort": SelectionSort(),
    "Quick Sort": QuickSort(),
    "Merge Sort": MergeSort(),
    "Tim Sort": TimSort(),
}