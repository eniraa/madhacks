import { writable } from "svelte/store";
import type { Writable } from "svelte/store";

export interface BackendResponse {
  coverage?: string;
  memory?: number; // bytes
  output?: string;
  success?: boolean;
  time?: number;
  analysis?: string;
  error?: string;
}

export const response: Writable<BackendResponse> = writable({});
//   {
//   analysis:
//     "Time complexity: O(n log n)\nThe program's time complexity can be explained by its overall structure. The program is split into two functions, count_sort and merge_count, and each function is called recursively. Because the algorithm divides and conquers the data, the time complexity can be judged as O(n log n).\n\nSpace complexity: O(n)\nThe program's space complexity can be judged as O(n), as there are several variables being used to store and process the data, and each of these variables require a certain amount of space. Additionally, the program creates a new list and populates it with elements from the list being sorted. This requires additional space to be allocated.",
//   coverage:
//     '    1: def merge_count(a, b):\n    4:     merged = []\n    4:     inversions = 0\n   16:     while len(a) != 0 or len(b) != 0:\n   12:         if len(b) == 0:\n    5:             merged.append(a[0])\n    5:             a.pop(0)\n    7:         elif len(a) == 0 or b[0] < a[0]:\n    7:             merged.append(b[0])\n    7:             inversions += len(a)\n    7:             b.pop(0)\n               else:\n                   merged.append(a[0])\n                   a.pop(0)\n    4:     return merged, inversions\n       \n       \n    1: def count_sort(list):\n    9:     if len(list) == 1:\n    5:         return list, 0\n    4:     halfway = len(list) // 2\n    4:     a1, ainv = count_sort(list[0:halfway])\n    4:     a2, ainv2 = count_sort(list[halfway:])\n       \n    4:     merge, minv = merge_count(a1, a2)\n       \n    4:     return merge, minv + ainv + ainv2\n       \n       \n    1: numbers = []\n    1: n = int(input())\n       \n    6: for i in range(0, n):\n    5:     numbers.append(int(input()))\n       \n    1: sorted_nums, inversions = count_sort(numbers)\n       \n    1: print(f"Sorted list: {sorted_nums}, {inversions} inversions")\n',
//   memory: 9381,
//   output: "Sorted list: [1, 2, 3, 4, 5], 10 inversions\n",
//   success: true,
//   time: 7.225000081234612e-5,
// });

// ({
//   error: "bruh moment",
//   success: true,
//   memory: 42069,
//   output: "Hello World!\n\n\n\nBye World!",
//   time: 0.000069,
//   coverage: "Not Covered By This Health Insurance Plan",
//   analysis: "This code runs in O(fuck) time",
// });
