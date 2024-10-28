# Project 29: Colorful Text Printer

Today’s challenge is to write a subroutine that prints text in color! By using ANSI color codes, you can create colorful output directly in the terminal. This subroutine will:

- Print text in a specified color.
- Control `end` and `sep` parameters to ensure no extra symbols or spaces appear.
- Reset the color back to normal once the text is printed.

### Steps

1. **Define a Color Subroutine**:
   - Create a function that takes `text` and a `color_code` as arguments.
   - Print the text with the specified color code and reset the terminal color after printing.

2. **Implement `end` and `sep` Controls**:
   - Add `end` and `sep` parameters in the function to control how the text output appears.

3. **Using ANSI Codes**:
   - Use [ANSI color codes](https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007) to set and reset colors. (e.g., `\033[31m` for red, `\033[0m` to reset)

---

## Output:
