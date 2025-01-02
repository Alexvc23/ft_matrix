# Enter the Matrix: An Introduction to Linear Algebra

Welcome to **Enter the Matrix**, a comprehensive educational project designed to introduce you to the fundamental concepts of linear algebra. This module covers theoretical foundations, practical coding exercises, and explores the rich connections between linear algebra and various fields such as computer science, physics, and data science.

## Overview

Linear algebra is a cornerstone of modern mathematics and its applications are vast, spanning areas such as:
- **Physics**: Mechanics, quantum mechanics, and relativity.
- **Computer Science**: Graphics, game development, and high-performance computing.
- **Data Science**: Machine learning, statistics, and big data analytics.

This project emphasizes practical learning through a series of exercises and challenges. It focuses on finite-dimensional vector spaces and their transformations, represented as matrices, with an emphasis on 2D and 3D spaces for better visualization.

## Key Features

- **Structured Learning**: Gradually build your understanding from basic vector operations to advanced topics like matrix decomposition and projection matrices.
- **Hands-On Coding**: Implement fundamental operations (e.g., addition, scaling, and dot products) and explore their applications.
- **Cross-Disciplinary Insights**: Learn how linear algebra underpins graphics rendering, machine learning, and statistical models.

## Prerequisites

- Basic arithmetic and familiarity with programming.
- (Optional) Prior exposure to Boolean algebra and abstract algebra is beneficial but not mandatory.

## Exercises and Topics

This project includes:
- Vector operations: addition, subtraction, scaling.
- Linear combinations, dot products, and norms.
- Matrix operations: multiplication, transposition, and inversion.
- Advanced topics: rank, projection matrices, and systems of linear equations.

The exercises are implemented in a generic programming framework, allowing flexibility in choosing the programming language. Support for Rust-like generic structures is recommended.

## Getting Started

1. Familiarize yourself with the provided theoretical content.
2. Watch the **Essence of Linear Algebra** video series by 3blue1brown for a visual introduction.
3. Start coding! Implement the exercises as described in the documentation.

## Theorical part
Absolutely, I'd be happy to explain vectors and matrices in simple terms! Let's break down each concept step by step, making it easy to understand even if you're encountering them for the first time.

---

## 1. What is a Vector ($\mathbf{v}$) ? 

### **a. Simple Definition**
A **vector** is a way to represent both a **magnitude** (size) and a **direction**. Think of it as an arrow pointing from one place to another.

### **b. Everyday Example**
Imagine you're giving someone directions: "Walk 3 blocks north and 4 blocks east." This direction can be represented as a vector because it has both length (how far) and direction (where to).

### **c. Mathematical Representation**
In math, a vector is usually written as an ordered list of numbers. For example:
- **2D Vector**: $[x, y] \,\,i.e\; \, [3, 4]$
- **3D Vector**: $[x, y, z] \,\,i.e\, \,[1, 5, 2]$

These numbers represent the vector's components along each axis (like north/south and east/west).

### **d. Visual Representation**
- **2D Vector**: Picture a flat graph with an x-axis (horizontal) and y-axis (vertical). A vector $[3, 4]$ starts at the origin (0,0) and points to the position (3,4).

    <details>
        <summary><b>Click to view 2D Vector Example</b></summary>
        <img src="./assets/ArrowDiagram.jpg" alt="2D Vector Example" width="50%" height="50%" />
    </details>

---

- **3D Vector**: Imagine adding a z-axis (depth) to the graph. A vector $[1, 5, 2]$ points into this three-dimensional space.

    <details>
        <summary><b>Click to view 3D Vector Example</b></summary>
        <img src="./assets/3d1.png" alt="2D Vector Example" width="50%" height="50%" />
        <img src="./assets/3d2.png" alt="2D Vector Example" width="50%" height="50%" />
    </details>

### **e. Uses in Algebra**
In algebra, vectors are used to solve systems of equations, represent points in space, and perform operations like addition and scalar multiplication (changing the size of the vector).

### **f. Uses in Computer Science**
Vectors are fundamental in computer graphics (representing positions and movements), machine learning (storing data as numerical lists), and physics simulations (modeling forces and velocities).


### The Components of a Vector from Its Endpoints


When you have a vector defined by two points 
$A(x_1, y_1)$  and $B(x_2, y_2)$, 
the most common way to find its components **(y-vertical-component and x-horizontal-component)** (in 2D) is to subtract the coordinates of \( A \) from the coordinates of \( B \). In other words:

$$
\overrightarrow{AB} = (\,x_2 - x_1, \; y_2 - y_1\,).
$$

- **(horizontal) X-component:** $x_2 - x_1$
- **(Vectical)Y-component:** $y_2 - y_1$


This pair of numbers tells you how far you move horizontally and vertically to go from \( A \) to \( B \).
 
1. If  $x_2 - x_1$ is **positive**, the vector moves to the **right**.  
2. If  $x_2 - x_1$ is **negative**, it moves to the **left**.  
3. If  $y_2 - y_1$ is **positive**, it moves **upward**.  
4. If  $y_2 - y_1$ is **negative**, it moves **downward**.

### Graphical Example

Consider points $A(1, 2)$ and $B(4, 6)$:

- **x-component:** $4 - 1 = 3$  
- **y-component:** $6 - 2 = 4$

The vector $\overrightarrow{AB}$ can be represented as $(3, 4)$.

<details>
    <summary><b>Click to view the graphical representation</b></summary>
    <img src="./assets/vector_AB.png" alt="Vector AB Example" width="50%" height="50%" />
    <p>
    In this diagram, the red point is A(1,2), the blue point is B(4,6), and the green arrow is the vector (3,4), highlighting its horizontal and vertical components.
    </p>
</details>


---

### **Calculating the Magnitude** $||\mathbf{v}||$

### **a. Simple Definition**
The **magnitude** of a vector measures its length or size. It tells you how long the vector is in space.

### **b. Everyday Example**
Imagine walking from your home to a friend's house. The distance you walk represents the magnitude of the displacement vector between the two points.

### **c. Mathematical Representation**
For a vector $\mathbf{v} = [x, y]$ in 2D or $\mathbf{v} = [x, y, z]$ in 3D, the **magnitude** $||\mathbf{v}||$ is calculated using the following formula:


- **2D Vector:**

$$
||\mathbf{v}|| = \sqrt{x^2 + y^2}
$$

- **3D Vector:**

$$
||\mathbf{v}|| = \sqrt{x^2 + y^2 + z^2}
$$

### **d. Example Calculation**

- **2D Example:**
    
    Consider the vector $\mathbf{v} = [3, 4] $.
    
$$
||\mathbf{v}|| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
$$

- **3D Example:**
    
    Consider the vector $\mathbf{u} = [1, 2, 2] $.
    
$$
||\mathbf{u}|| = \sqrt{1^2 + 2^2 + 2^2} = \sqrt{1 + 4 + 4} = \sqrt{9} = 3
$$

### **e. Visual Representation**

<details>
    <summary><b>Click to view Vector Magnitude Examples</b></summary>

<h5>2D Vector Magnitude:</h5>

<p align="center">
    <img src="./assets/vector_magnitude_2d.png" alt="Vector Magnitude 2D" width="50%" height="50%">
</p>
<p><i>The length of the arrow represents the magnitude of the vector.</i></p>

<h5>3D Vector Magnitude:</h5>
<p align="center">
    <img src="./assets/vector_magnitude_3d.png" alt="Vector Magnitude 3D" width="50%" height="50%">
</p>
<p><i>The length of the arrow in three-dimensional space indicates the vector's magnitude.</i></p>

</details>

---
## Vector Addition and Subtraction:

### Basic Operations

#### Vector Addition
To add two vectors, add their corresponding components:

$$
\begin{aligned}
\mathbf{u} &= [2, 3] \\
\mathbf{v} &= [4, 1] \\
\mathbf{u} + \mathbf{v} &= [2+4, 3+1] = [6, 4]
\end{aligned}
$$

### 👀 Visual Representation

<details>
    <summary><b> 🌄 Click to view Vector Addition Example</b></summary>
    <img src="./assets/vector_addition.png" alt="Vector Addition" width="50%" height="50%" />
</details>

#### Vector Subtraction
To subtract vectors, subtract their corresponding components:


$$
\begin{aligned}
\mathbf{u} &= [5, 7] \\
\mathbf{v} &= [2, 3] \\
\mathbf{u} - \mathbf{v} &= [5-2, 7-3] = [3, 4]
\end{aligned}
$$

Here's another example with a negative vector:


$$
\begin{aligned}
\mathbf{u} &= [-2, 4] \\
\mathbf{v} &= [3, -1] \\
\mathbf{u} - \mathbf{v} &= [-2-3, 4-(-1)] = [-5, 5]
\end{aligned}
$$

### 👀 Visual Representation

<details>
    <summary><b> 🌄 Click to view Vector Addition Example</b></summary>
    <img src="./assets/vector_subtraction.png" alt="Vector Addition" width="50%" height="50%" />
</details>


### Key Properties

- Addition is commutative: `u + v = v + u`
- Subtraction is not commutative: `u - v ≠ v - u`
- Zero vector addition: `v + [0,0] = v`

----

## Scalar Multiplication

### **a. Simple Definition**
**Scalar Multiplication** is when you multiply a vector by a single number (scalar), affecting its magnitude but not its direction (unless negative).

### **b. Mathematical Representation**
For a scalar $a$ and vector $\mathbf{v}$:

$$
a\mathbf{v} = [ax_1, ax_2, ..., ax_n]
$$

### **c. Example**
Given vector $\mathbf{v} = [2, 3]$ and scalar $a = 4$:

$$
4 \times [2, 3] = [8, 12]
$$

### d. Visual Representation
<details>
    <summary><b> Click to view Scalar Multiplication Example</b></summary>
    <p align="center">
        <img src="./assets/scalar_mult.png" alt="Scalar Multiplication" width="50%" height="50%" />
    </p>
    
- 🔵 The blue arrow represents the original vector $[2,3]$.
- 🟢 The green arrow represents the scaled vector $[8,12]$, obtained by multiplying the original vector by 4.
</details>

---

## **2. What is a Matrix?**

### **a. Simple Definition**
A **matrix** is a rectangular array of numbers arranged in rows and columns. You can think of it as a spreadsheet with multiple rows and columns.

### **b. Everyday Example**
Imagine an Excel spreadsheet where each cell contains a number. This grid of numbers is similar to a matrix.

### **c. Mathematical Representation**
A matrix is written using brackets with rows and columns. For example, a 2x3 matrix (2 rows and 3 columns) looks like this:

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{bmatrix}
$$

### **d. Visual Representation**
Think of a matrix as a table:

|   | Column 1 | Column 2 | Column 3 |
|---|:--------:|:--------:|:--------:|
| **Row 1** |    1     |     2    |     3    |
| **Row 2** |    4     |     5    |     6    |

### **e. Uses in Algebra**
In algebra, matrices are used to solve systems of equations, perform linear transformations (like rotating or scaling shapes), and represent data in a structured form.

### **f. Uses in Computer Science**
Matrices are essential in computer graphics (transforming images), machine learning (handling large datasets), network analysis, and solving complex algorithms efficiently.

---

## **3. How Do Vectors and Matrices Work Together?**

### **a. Combining Vectors**
You can add vectors together or multiply them by numbers (scalars) to change their size or direction.

**Vector Addition Example:**

$$
\begin{bmatrix}
1 \\
2 \\
\end{bmatrix}
+
\begin{bmatrix}
3 \\
4 \\
\end{bmatrix} =
\begin{bmatrix}
4 \\
6 \\
\end{bmatrix}
$$

### **b. Matrix Operations: Addition and Subtraction**

In matrix operations, we can add and subtract matrices of the same dimensions. Let's explore these fundamental operations.

#### Addition Example:
Given two 2×2 matrices:

$$
A = \begin{bmatrix}
1 & 2 \\
3 & 4 \\
\end{bmatrix}, \quad
B = \begin{bmatrix}
5 & 6 \\
7 & 8 \\
\end{bmatrix}
$$

Add corresponding elements:

$$
A + B = \begin{bmatrix}
1+5 & 2+6 \\
3+7 & 4+8 \\
\end{bmatrix} = \begin{bmatrix}
6 & 8 \\
10 & 12 \\
\end{bmatrix}
$$

#### Subtraction Example:
Matrix subtraction can be expressed as: A - B = A + (-1)⋅B

Given two 2×2 matrices:

$$
A = \begin{bmatrix}
3 & 5 \\
7 & 9 \\
\end{bmatrix}, \quad
B = \begin{bmatrix}
1 & 2 \\
4 & 6 \\
\end{bmatrix}
$$

First, calculate (-1)⋅B:

$$
(-1)⋅B = \begin{bmatrix}
-1 & -2 \\
-4 & -6 \\
\end{bmatrix}
$$

Then add A and (-1)⋅B:

$$
A - B = \begin{bmatrix}
3-1 & 5-2 \\
7-4 & 9-6 \\
\end{bmatrix} = \begin{bmatrix}
2 & 3 \\
3 & 3 \\
\end{bmatrix}
$$

Remember:
- **<span style="color:red">Matrices must have the same dimensions</span>**
- Operations are performed element by element
- These operations form the basis for more complex matrix transformations

---

## **4. Practical Applications**

### **a. Computer Graphics**
- **Vectors** represent points, directions, and movements in 2D or 3D space.
- **Matrices** perform transformations like rotation, scaling, and translation of images and models.

### **b. Machine Learning**
- **Vectors** store features or data points (e.g., characteristics of a house: size, number of rooms).
- **Matrices** represent datasets where each row is a data point and each column is a feature.

---

## **5. Key Takeaways**

- **Vectors** are ordered lists of numbers representing magnitude and direction. They're like arrows in space or lists of data.
  
- **Matrices** are grids of numbers arranged in rows and columns. They're like spreadsheets or tables of data.

- Both vectors and matrices are fundamental tools in both **algebra** and **computer science**, enabling the representation and manipulation of complex data and transformations.

- Understanding vectors and matrices opens the door to more advanced topics in mathematics, programming, and various scientific fields.

---


## Resources

- [Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) by 3blue1brown.
- Additional reading: [Wikipedia - Vector Space](https://en.wikipedia.org/wiki/Vector_space)

## Contributing

This is a peer-learning project. Collaborate with your peers, review their code, and refine your understanding through feedback.

## Submission Guidelines

Submit your completed code in your Git repository as per the project guidelines. Ensure all files are correctly named and organized.

---

Dive into the world of vectors and matrices, and unlock the power of linear algebra!
