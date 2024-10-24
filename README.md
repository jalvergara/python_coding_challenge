# 🐑 Counting Sheep - Python Challenge

## 🌟 Problem Description

Bleatrix the sheep has trouble falling asleep. To help her, she picks a number `N` and starts counting its multiples in the following order: `N`, `2N`, `3N`, and so on. As she counts, she tracks which digits (0-9) she has seen in these multiples.

The goal is to determine the last multiple Bleatrix will see before she has encountered all digits at least once, or if Bleatrix never sees all digits, she will suffer from **INSOMNIA**.

### Example:

For `N = 1692`, Bleatrix would count:

- 1692 → Seen digits: [1, 6, 9, 2]
- 3384 → Seen digits: [1, 6, 9, 2, 3, 8, 4]
- 5076 → Seen all digits: [1, 6, 9, 2, 3, 8, 4, 5, 0, 7]

Bleatrix falls asleep after counting **5076**.

If Bleatrix chooses `N = 0`, she will never see all digits, and the result will be **INSOMNIA**.

## 📊 Results Obtained

We ran several test cases, and all generated outputs were successfully verified. The program stayed within the time and memory limits for all test cases, as shown below:


### Test Results Summary:

```
INFO:root:[INFO] Memory usage: 67.31 MB
INFO:root:[INFO] Execution time of generate_output: 0.0042 seconds
../output/test1_out.ans: SUCCEED
```
```
INFO:root:[INFO] Memory usage: 67.31 MB
INFO:root:[INFO] Execution time of generate_output: 0.0050 seconds
../output/test2_out.ans: SUCCEED
```
```
INFO:root:[INFO] Memory usage: 67.31 MB
INFO:root:[INFO] Execution time of generate_output: 0.0020 seconds
../output/test3_out.ans: SUCCEED
```


- **Execution time** for each test case set: ⏱ **< 10 seconds**
- **Memory usage**: 🧠 **< 1 GB**

## 📂 Project Structure

Here’s how the project is structured:

```
📂 context/
    ├── examples/
    |   ├── sample.ans
    |   ├── sample.in
    |   ├── test1.in
    |   ├── test2.in
    |   ├── test3.in
    └── notebooks/
    |   └── 01_counting_sheep_implementation.ipynb
    └── output/
        ├── sample_out.ans
        ├── test1_out.ans
        ├── test2_out.ans
        ├── test3_out.ans
📂 src/
    ├── metrics.py
    └── sheepfunctions.py
.gitignore
pyproject.toml
README.md
```

## 🚀 How to Run the Project

### Prerequisites

Ensure you have **Poetry** installed to manage dependencies. If you don't have it, you can install it following the instructions on [Poetry's official website](https://python-poetry.org/docs/#installation).

### Steps to Run:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/counting-sheep-challenge.git
   cd counting-sheep-challenge
   ```

2. **Install the dependencies**:

   Inside the project directory, run:

   ```bash
   poetry install
   ```

3. **Run the tests**:

   To generate the output files for the test cases:

   ```bash
   poetry run python src/sheepfunctions.py
   ```

4. **Check the results**:

   The outputs will be generated in the `output/` folder, and you can compare them with the expected results in the `examples/` folder.

### Running Jupyter Notebook

If you want to use Jupyter Notebooks, open the notebook provided in the project using:

```bash
poetry run jupyter notebook
```

Then, navigate to the `notebooks/01_counting_sheep_implementation.ipynb` file and execute the cells interactively.

## 🛠 Dependencies

The project uses the following Python dependencies:

- **Python 3.12**
- **word2number**
- **psutil**

These dependencies will be installed automatically with `poetry install`.

## 💡 Additional Notes

- **Time limit** for processing each test set: ⏱ **10 seconds**
- **Memory limit** for processing: 🧠 **1 GB**

Feel free to contribute or suggest improvements! 🚀

---