#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  // ==========================================
  // CASE 1: IMMUTABILITY & ASSIGNMENT (The "Sealed Stone")
  // Python equivalent:
  // x = 10
  // x = 20
  // ==========================================
  printf("--- CASE 1: ASSIGNMENT (Rebinding) ---\n");

  // 1. Create two "Integer Objects" in memory (Sealed Stones)
  int object_10 = 10;
  int object_20 = 20;

  // 2. Create the Python Name 'x' (A Pointer) pointing to the first object
  // Python: x = 10
  int *x = &object_10; // the variable x holds the address of object_10
  printf("Step 1: x points to address %p which holds value: %d\n", (void *)x,
         *x); // Dereference to get the value

  // 3. Perform Assignment (The '=' operator)
  // Python: x = 20
  // NOTICE: We do NOT change the value inside object_10.
  // We simply move the pointer 'x' to a different address.
  x = &object_20;
  printf("Step 2: x points to address %p which holds value: %d\n", (void *)x,
         *x);

  printf("(Notice: The pointer address CHANGED. 'x' is now looking at a "
         "different stone.)\n\n");

  // ==========================================
  // CASE 2: MUTATION (The "Open Box")
  // Python equivalent:
  // lst = [10]
  // lst[0] = 99
  // ==========================================
  printf("--- CASE 2: MUTATION (Modifying In-Place) ---\n");

  // 1. Create a "List Object" in memory (An Open Box)
  // We malloc memory so it's a stable container in the heap.
  // Allocate space for 2 integers
  int *lst = (int *)malloc(sizeof(int) * 2);
  *lst = 10; // Put 10 inside the box
  // Add second value to the second element int he array
  *(lst + 1) = 20;

  printf("Step 1: lst points to address %p which holds value: %d\n",
         (void *)lst, *lst);

  // 2. Perform Mutation (The '[]' or 'append' operator)
  // Python: lst[0] = 99
  // NOTICE: We do NOT move the pointer 'lst'. We keep looking at the SAME
  // address. We reach INSIDE that address and change the data.
  *lst = 99;

  printf("Step 2: lst points to address %p which holds value: %d\n",
         (void *)lst, *lst);

  printf("(Notice: The pointer address STAYED THE SAME. The contents inside "
         "changed.)\n");

  printf("Also, the second element in the list is still: %d\n", *(lst + 1));
  printf("the address of the second element is: %p\n", (void *)(lst + 1));

  free(lst); // Clean up
  return 0;
}
