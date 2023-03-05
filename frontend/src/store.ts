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

export const response: Writable<BackendResponse> = writable({
  error: "bruh moment",
  success: true,
  memory: 42069,
  output: "Hello World!\n\n\n\nBye World!",
  time: 0.000069,
  coverage: "Not Covered By This Health Insurance Plan",
  analysis: "This code runs in O(fuck) time",
});
