
## Table of Contents

1.  [Enter the Matrix: An Introduction to Linear Algebra](#enter-the-matrix-an-introduction-to-linear-algebra)
2.  [Overview](#overview)
3.  [Goal of this project](#goal-of-this-project)
4.  [Exercises and Topics](#exercises-and-topics)
5.  [Getting Started](#getting-started)
6.  [1. What is a Vector?](#1-what-is-a-vector)
    *   [a. Simple Definition](#a-simple-definition)
    *   [b. Everyday Example](#b-everyday-example)
    *   [c. Mathematical Representation](#c-mathematical-representation)
    *   [d. Visual Representation](#d-visual-representation)
    *   [e. Uses in Algebra](#e-uses-in-algebra)
    *   [f. Uses in Computer Science](#f-uses-in-computer-science)
    *   [The Components of a Vector from Its Endpoints](#the-components-of-a-vector-from-its-endpoints)
    *   [Graphical Example](#graphical-example)
    *   [Calculating the Magnitude ||**v**||](#calculating-the-magnitude-v)
        *   [a. Simple Definition](#a-simple-definition-1)
        *   [b. Everyday Example](#b-everyday-example-1)
        *   [c. Mathematical Representation](#c-mathematical-representation-1)
        *   [d. Example Calculation](#d-example-calculation)
        *   [e. Visual Representation](#e-visual-representation)
7.  [2. What is a Matrix?](#2-what-is-a-matrix)
    *   [a. Simple Definition](#a-simple-definition-2)
    *   [b. Everyday Example](#b-everyday-example-2)
    *   [c. Mathematical Representation](#c-mathematical-representation-2)
    *   [d. Visual Representation](#d-visual-representation-1)
    *   [e. Uses in Algebra](#e-uses-in-algebra-1)
    *   [f. Uses in Computer Science](#f-uses-in-computer-science-1)
8.  [Ex 00](#ex-00)
    *   [Vector Addition and Subtraction](#vector-addition-and-subtraction)
        *   [Basic Operations](#basic-operations)
            *   [Vector Addition](#vector-addition)
            *   [Visual Representation (Addition)](#visual-representation-2)
            *   [Vector Subtraction](#vector-subtraction)
            *   [Visual Representation (Subtraction)](#visual-representation-3)
        *   [Key Properties](#key-properties)
    *   [Scalar Multiplication](#scalar-multiplication)
        *   [Simple Definition](#simple-definition)
        *   [Mathematical Representation](#mathematical-representation-3)
        *   [Example](#example)
        *   [Visual Representation](#visual-representation-4)
    *   [Matrix Operations: Addition and Subtraction](#matrix-operations-addition-and-subtraction)
        *   [Addition Example](#addition-example)
        *   [Subtraction Example](#subtraction-example)
        *   [Key Properties](#key-properties-1)
9.  [Ex 01](#ex-01)
    *   [What's a Linear Combination?](#whats-a-linear-combination)
        *   [Example](#example-1)
        *   [Calculation](#calculation)
        *   [Real-World Applications](#real-world-applications)
        *   [Inputs of the Function](#inputs-of-the-function)
        *   [Output](#output)
        *   [How the Function Works](#how-the-function-works)
        *   [Example (Function)](#example-2)
        *   [Efficiency](#efficiency)
        *   [Constraints](#constraints)
10. [Ex 02](#ex-02)
    *   [Linear Interpolation](#linear-interpolation)
        *   [Definition](#definition)
        *   [Example Calculation](#example-calculation-1)
        *   [Visual Representation](#visual-representation-5)
        *   [Vector Interpolation](#vector-interpolation)
        *   [Example with Vectors](#example-with-vectors)
        *   [Applications](#applications)
        *   [Implementation Considerations](#implementation-considerations)
11. [Ex 03](#ex-03)
    *   [The Dot Product](#the-dot-product)
        *   [Definition](#definition-1)
        *   [Example Calculation](#example-calculation-2)
        *   [Geometric Interpretation](#geometric-interpretation)
        *   [Properties](#properties)
        *   [Applications](#applications-1)
        *   [Implementation Considerations](#implementation-considerations-1)
12. [Ex 04](#ex-04)
    *   [Norm (Vector Length)](#norm-vector-length)
        *   [Types of Norms](#types-of-norms)
            *   [L1 Norm (Manhattan Norm)](#l1-norm-manhattan-norm)
            *   [L2 Norm (Euclidean Norm)](#l2-norm-euclidean-norm)
            *   [Infinity Norm (Max Norm)](#infinity-norm-max-norm)
        *   [Example Calculations](#example-calculations)
        *   [Visual Representation](#visual-representation-6)
        *   [Properties](#properties-1)
        *   [Applications](#applications-2)
        *   [Implementation Notes](#implementation-notes)
13. [Ex 05](#ex-05)
    *   [Cosine Similarity](#cosine-similarity)
        *   [In Simple Terms](#in-simple-terms)
        *   [Definition](#definition-2)
        *   [Interpretation](#interpretation)
        *   [Example Calculation](#example-calculation-3)
        *   [Visual Representation](#visual-representation-7)
        *   [Applications](#applications-3)
        *   [Implementation Considerations](#implementation-considerations-2)
14. [Ex 06](#ex-06)
    *   [The Cross Product](#the-cross-product)
        *   [Definition](#definition-3)
        *   [Determinant Calculation Method](#determinant-calculation-method)
        *   [Geometric Interpretation](#geometric-interpretation-1)
        *   [Example Calculation](#example-calculation-4)
        *   [Properties](#properties-2)
        *   [Applications](#applications-4)
        *   [Implementation Considerations](#implementation-considerations-3)
15. [Ex 07](#ex-07)
    *   [Matrix Multiplication](#matrix-multiplication)
        *   [Definition](#definition-4)
        *   [Compatibility Requirement](#compatibility-requirement)
        *   [Formula](#formula)
        *   [Example Calculation](#example-calculation-5)
        *   [Matrix-Vector Example](#matrix-vector-example)
        *   [Properties](#properties-3)
        *   [Applications](#applications-5)
        *   [Implementation Considerations](#implementation-considerations-4)
16. [Ex 08](#ex-08)
    *   [Trace](#trace)
        *   [Definition](#definition-5)
        *   [Compatibility Requirement](#compatibility-requirement-1)
        *   [Example Calculation](#example-calculation-6)
        *   [Properties](#properties-4)
        *   [Applications](#applications-6)
        *   [Implementation Considerations](#implementation-considerations-5)
17. [Ex 09](#ex-09)
    *   [Transpose](#transpose)
        *   [Definition](#definition-6)
        *   [Compatibility Requirement](#compatibility-requirement-2)
        *   [Example Calculation](#example-calculation-7)
        *   [Properties](#properties-5)
        *   [Applications](#applications-7)
        *   [Implementation Considerations](#implementation-considerations-6)
18. [Ex 10](#ex-10)
    *   [Row Echelon Form](#row-echelon-form)
        *   [Elementary Row Operations](#elementary-row-operations)
        *   [Criteria for Row Echelon Form (REF)](#criteria-for-row-echelon-form-ref)
        *   [Example (Correct REF)](#example-correct-ref)
        *   [Example (Incorrect REF)](#example-incorrect-ref)
        *   [Example Calculation (Gaussian Elimination to REF)](#example-calculation-gaussian-elimination-to-ref)
        *   [Reduced Row Echelon Form (RREF)](#reduced-row-echelon-form-rref)
        *   [Applications](#applications-8)
        *   [Implementation Considerations](#implementation-considerations-7)
    *   [2. Why REF Matters](#2-why-ref-matters)
        *   [Example (Computing Rank)](#example-computing-rank)

---

# Enter the Matrix: An Introduction to Linear Algebra

Welcome to **Enter the Matrix**, a comprehensive educational project designed to introduce you to the fundamental concepts of linear algebra. This module covers theoretical foundations, practical coding exercises, and explores the rich connections between linear algebra and various fields such as computer science, physics, and data science.

## Overview

Linear algebra is a cornerstone of modern mathematics and its applications are vast, spanning areas such as:
- **Physics**: Mechanics, quantum mechanics, and relativity.
- **Computer Science**: Graphics, game development, and high-performance computing.
- **Data Science**: Machine learning, statistics, and big data analytics.

This project emphasizes practical learning through a series of exercises and challenges. It focuses on finite-dimensional vector spaces and their transformations, represented as matrices, with an emphasis on 2D and 3D spaces for better visualization.

## Goal of this project 

- **Structured Learning**: Gradually build your understanding from basic vector operations to advanced topics like matrix decomposition and projection matrices.
- **Hands-On Coding**: Implement fundamental operations (e.g., addition, scaling, and dot products) and explore their applications.
- **Cross-Disciplinary Insights**: Learn how linear algebra underpins graphics rendering, machine learning, and statistical models.


## Exercises and Topics

This project includes:
- Vector operations: addition, subtraction, scaling.
- Linear combinations, dot products, and norms.
- Matrix operations: multiplication, transposition, and inversion.
- Advanced topics: rank, projection matrices, and systems of linear equations.

## Getting Started

1. Familiarize yourself with the provided theoretical content.
2. Watch the **Essence of Linear Algebra** video series by 3blue1brown for a visual introduction.
3. Start coding! Implement the exercises as described in the documentation.

---

## 1. What is a Vector?

### a. Simple Definition
A **vector** is a way to represent both a **magnitude** (size) and a **direction**. Think of it as an arrow pointing from one place to another.

### b. Everyday Example
Imagine you're giving someone directions: "Walk 3 blocks north and 4 blocks east." This direction can be represented as a vector because it has both length (how far) and direction (where to).

### c. Mathematical Representation
In math, a vector is usually written as an ordered list of numbers. For example:
- **2D Vector**: $[x, y] \,\,i.e\; \, [3, 4]$
- **3D Vector**: $[x, y, z] \,\,i.e\, \,[1, 5, 2]$

These numbers represent the vector's components along each axis (like north/south and east/west).

### d. Visual Representation
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

### e. Uses in Algebra
In algebra, vectors are used to solve systems of equations, represent points in space, and perform operations like addition and scalar multiplication (changing the size of the vector).

### f. Uses in Computer Science
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


<details>
    <summary><b>Click to view the graphical representation</b></summary>
    <img src="./assets/vector_AB.png" alt="Vector AB Example" width="50%" height="50%" />
    <p>
    In this diagram, the red point is A(1,2), the blue point is B(4,6), and the green arrow is the vector (3,4), highlighting its horizontal and vertical components.
    </p>
</details>

---

### Calculating the Magnitude $||\mathbf{v}||$

#### a. Simple Definition
The **magnitude** of a vector measures its length or size. It tells you how long the vector is in space.

#### b. Everyday Example
Imagine walking from your home to a friend's house. The distance you walk represents the magnitude of the displacement vector between the two points.

#### c. Mathematical Representation
For a vector $\mathbf{v} = [x, y]$ in 2D or $\mathbf{v} = [x, y, z]$ in 3D, the **magnitude** $||\mathbf{v}||$ is calculated using the following formula:

- **2D Vector:**

$$
||\mathbf{v}|| = \sqrt{x^2 + y^2}
$$

- **3D Vector:**

$$
||\mathbf{v}|| = \sqrt{x^2 + y^2 + z^2}
$$

#### d. Example Calculation

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

#### e. Visual Representation

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

## 2. What is a Matrix?

### a. Simple Definition
A **matrix** is a rectangular array of numbers arranged in rows and columns. You can think of it as a spreadsheet with multiple rows and columns.

### b. Everyday Example
Imagine an Excel spreadsheet where each cell contains a number. This grid of numbers is similar to a matrix.

### c. Mathematical Representation
A matrix is written using brackets with rows and columns. For example, a 2x3 matrix (2 rows and 3 columns) looks like this:

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
\end{bmatrix}
$$

### d. Visual Representation
Think of a matrix as a table:

|   | Column 1 | Column 2 | Column 3 |
|---|:--------:|:--------:|:--------:|
| **Row 1** |    1     |     2    |     3    |
| **Row 2** |    4     |     5    |     6    |

### e. Uses in Algebra
In algebra, matrices are used to solve systems of equations, perform linear transformations (like rotating or scaling shapes), and represent data in a structured form.

### f. Uses in Computer Science
Matrices are essential in computer graphics (transforming images), machine learning (handling large datasets), network analysis, and solving complex algorithms efficiently.

---
# Ex 00

## Vector Addition and Subtraction

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

#### Visual Representation

<details>
    <summary><b>Click to view Vector Addition Example</b></summary>
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

#### Visual Representation

<details>
    <summary><b>Click to view Vector Subtraction Example</b></summary>
    <img src="./assets/vector_subtraction.png" alt="Vector Subtraction" width="50%" height="50%" />
</details>

### Key Properties

- Addition is commutative: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
- Subtraction is not commutative: $\mathbf{u} - \mathbf{v} \neq \mathbf{v} - \mathbf{u}$
- Zero vector addition: $\mathbf{v} + [0,0] = \mathbf{v}$

## Scalar Multiplication

### Simple Definition
**Scalar Multiplication** is when you multiply a vector by a single number (scalar), affecting its magnitude but not its direction (unless negative).

### Mathematical Representation
For a scalar $a$ and vector $\mathbf{v}$:

$$
a\mathbf{v} = [ax_1, ax_2, ..., ax_n]
$$

### Example
Given vector $\mathbf{v} = [2, 3]$ and scalar $a = 4$:

$$
4 \times [2, 3] = [8, 12]
$$

### Visual Representation
<details>
    <summary><b>Click to view Scalar Multiplication Example</b></summary>
    <p align="center">
        <img src="./assets/scalar_mult.png" alt="Scalar Multiplication" width="50%" height="50%" />
    </p>
    <ul>
        <li>🔵 The blue arrow represents the original vector $[2,3]$.</li>
        <li>🟢 The green arrow represents the scaled vector $[8,12]$, obtained by multiplying the original vector by 4.</li>
    </ul>
</details>

## Matrix Operations: Addition and Subtraction

### Addition Example
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

### Subtraction Example
Matrix subtraction can be expressed as: $A - B = A + (-1)⋅B$

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

First, calculate $(-1)⋅B$:

$$
(-1)⋅B = \begin{bmatrix}
-1 & -2 \\
-4 & -6 \\
\end{bmatrix}
$$

Then add $A$ and $(-1)⋅B$:

$$
A - B = \begin{bmatrix}
3-1 & 5-2 \\
7-4 & 9-6 \\
\end{bmatrix} = \begin{bmatrix}
2 & 3 \\
3 & 3 \\
\end{bmatrix}
$$

### Key Properties

- Matrices must have the same dimensions.
- Operations are performed element by element.
- These operations form the basis for more complex matrix transformations.

-------------------------------------------------------------------------

# ex 01

## What's a Linear Combination?

A linear combination involves taking several vectors and scaling each one by a number (called a scalar), then adding them up. For instance:

To understand the linear combination, let's break it down step by step:

### Example

Given vectors and scalars:
- Vectors: $\mathbf{u_1} = [1, 0, 0]$, $\mathbf{u_2} = [0, 1, 0]$
- Scalars: $a = 2$, $b = 3$

### Calculation

1. **Scale each vector by its corresponding scalar:**

$$
a \times \mathbf{u_1} = 2 \times [1, 0, 0] = [2, 0, 0]
$$

$$
b \times \mathbf{u_2} = 3 \times [0, 1, 0] = [0, 3, 0]
$$

2. **Add the scaled vectors:**

$$
\text{Result} = [2, 0, 0] + [0, 3, 0] = [2, 3, 0]
$$

So, the linear combination of the vectors $\mathbf{u_1}$ and $\mathbf{u_2}$ with scalars $a$ and $b$ is:

$$
\text{Result} = (2 \times [1, 0, 0]) + (3 \times [0, 1, 0]) = [2, 0, 0] + [0, 3, 0] = [2, 3, 0]
$$

### Real-World Applications

Linear combinations are crucial in:
- **Computer Graphics**: Blending colors or positions
- **Physics**: Calculating forces or velocities
- **Economics**: Portfolio optimization
- **Signal Processing**: Combining waveforms

### Inputs of the Function

- A list of vectors (e.g., `u = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]`).
- A list of scalars (e.g., `λ = [10, -2, 0.5]`).

### Output

- A single vector that is the result of applying the scalars to the corresponding vectors and summing them up.

### How the Function Works

- Multiply each vector by its corresponding scalar.
- Add the resulting scaled vectors together.

### Example

- Input vectors: `u = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]`.
- Scalars: `λ = [10, -2, 0.5]`.
- Result:

$$
(10 \times [1, 0, 0]) + (-2 \times [0, 1, 0]) + (0.5 \times [0, 0, 1]) = [10, -2, 0.5]
$$

### Efficiency

- The problem states that the solution must have a complexity of $O(n)$, where $n$ is the total number of numbers in all the vectors combined. <span style="color:red"> This means your solution should process each coordinate exactly once</span>.

### Constraints

- All vectors must have the same dimension.
- The number of scalars must match the number of vectors.
- Scalars and vector components should be real numbers.

# Ex 02

## Linear Interpolation

Linear interpolation (often abbreviated as "lerp") is a method of curve fitting using linear polynomials to construct new data points within the range of a discrete set of known data points.

### Definition

Linear interpolation connects two known points with a straight line and finds points along that line. The formula for linear interpolation between two points is:

$$
\text{lerp}(a, b, t) = a + t \times (b - a)
$$

Where:
- $a$ is the starting value
- $b$ is the ending value
- $t$ is the interpolation parameter (typically between 0 and 1)

### Example Calculation

If we want to find a point 30% of the way from 10 to 20:

$$
\text{lerp}(10, 20, 0.3) = 10 + 0.3 \times (20 - 10) = 10 + 0.3 \times 10 = 10 + 3 = 13
$$

### Visual Representation

<details>
    <summary><b>Click to view Linear Interpolation Example</b></summary>
    <img src="./assets/linear_interpolation.png" alt="Linear Interpolation" width="50%" height="50%" />
    <p><i>The blue line represents linear interpolation between points A and B. Parameter t controls the position along this line.</i></p>
</details>

### Vector Interpolation

Linear interpolation works with vectors by applying the formula to each component:

For vectors $\mathbf{v_1} = [a_1, a_2, ..., a_n]$ and $\mathbf{v_2} = [b_1, b_2, ..., b_n]$:

$$
\text{lerp}(\mathbf{v_1}, \mathbf{v_2}, t) = [a_1 + t(b_1 - a_1), a_2 + t(b_2 - a_2), ..., a_n + t(b_n - a_n)]
$$

### Example with Vectors

If $\mathbf{v_1} = [1, 2, 3]$ and $\mathbf{v_2} = [4, 5, 6]$ with $t = 0.5$:

$$
\begin{aligned}
\text{lerp}(\mathbf{v_1}, \mathbf{v_2}, 0.5) &= [1 + 0.5(4-1), 2 + 0.5(5-2), 3 + 0.5(6-3)] \\
&= [1 + 0.5 \times 3, 2 + 0.5 \times 3, 3 + 0.5 \times 3] \\
&= [1 + 1.5, 2 + 1.5, 3 + 1.5] \\
&= [2.5, 3.5, 4.5]
\end{aligned}
$$

### Applications

- **Computer Graphics**: Smoothly transitioning between positions, colors, or rotations
- **Animation**: Creating in-between frames for smooth movement
- **Data Visualization**: Generating color gradients or smooth transitions
- **Finance**: Approximating values between known data points

### Implementation Considerations

- Parameter $t$ is not restricted to [0,1], but values in this range interpolate between the points
- When $t = 0$, the result equals the first point
- When $t = 1$, the result equals the second point
- The vectors must have the same dimension
- The operation has linear time complexity O(n), where n is the dimension of the vectors

# Ex 03

## The Dot Product

The dot product is a fundamental operation between two vectors that results in a scalar value. It's also called the scalar product or inner product.

### Goals of the Dot Product

- **Measure similarity between vectors**: The dot product tells you how much two vectors point in the same direction
- **Find angles between vectors**: The dot product formula can be rearranged to calculate angles
- **Create linear transformations**: The dot product enables projection operations that form the basis of many linear transformations

### Why We Calculate the Dot Product

- **Quantifies vector relationships:** The scalar result provides a single number that measures how vectors interact
- **Simplifies complexity:** Reduces multidimensional vector relationships into a meaningful magnitude
- **Enables algebraic operations:** Allows for mathematical operations that wouldn't be possible with vector results

### Definition

For two vectors $\mathbf{u} = [u_1, u_2, ..., u_n]$ and $\mathbf{v} = [v_1, v_2, ..., v_n]$, their dot product is:

$$
\mathbf{u} \cdot \mathbf{v} = u_1 \times v_1 + u_2 \times v_2 + ... + u_n \times v_n = \sum_{i=1}^{n} u_i v_i
$$

### Example Calculation

If $\mathbf{u} = [1, 2, 3]$ and $\mathbf{v} = [4, 5, 6]$:

$$
\mathbf{u} \cdot \mathbf{v} = (1 \times 4) + ( 2 \times 5 )+ ( 3 \times 6) = 4 + 10 + 18 = 32
$$

### Geometric Interpretation

The dot product has a geometric meaning:

$$
\mathbf{u} \cdot \mathbf{v} = ||\mathbf{u}|| \times ||\mathbf{v}|| \times \cos(\theta)
$$

Where:
- $||\mathbf{u}||$ and $||\mathbf{v}||$ are the magnitudes of the vectors
- $\theta$ is the angle between them

<details>
    <summary><b>Click to view Geometric Representation</b></summary>
    <img src="./assets/dot_product.png" alt="Dot Product Geometry" width="50%" height="50%" />
    <img src="./assets/dot_product_linear_transformation.png" alt="Dot Product Linear Transformation" width="50%" height="50%" />
    <p><i>The dot product geometrically represents how much of one vector points in the direction of another, scaled by their magnitudes.</i></p>
</details>
</details>



### Dot Product vs. Cosine Similarity: Key Differences

The dot product and cosine similarity are related mathematical operations that measure relationships between vectors, but they serve different purposes and have distinct properties.

#### Dot Product

- **What it measures**: Both direction alignment AND magnitude of vectors
- **Formula**: $\mathbf{v} \cdot \mathbf{w} = \sum_{i=1}^{n} v_i w_i = \|\mathbf{v}\| \|\mathbf{w}\| \cos\theta$
- **Magnitude dependence**: If you double the length of one vector, the dot product doubles too
- **Range**: From $-\|\mathbf{v}\|\|\mathbf{w}\|$ to $+\|\mathbf{v}\|\|\mathbf{w}\|$
- **Best for**: Problems where both direction and magnitude matter (like calculating physical work or energy)

#### Cosine Similarity 

- **What it measures**: ONLY direction alignment between vectors
- **Formula**: $\text{cosine\_similarity}(\mathbf{v},\mathbf{w}) = \frac{\mathbf{v} \cdot \mathbf{w}}{\|\mathbf{v}\| \|\mathbf{w}\|} = \cos\theta$
- **Magnitude dependence**: None - scaling vectors doesn't change the result
- **Range**: Always between -1 and +1
    - +1: vectors point in identical directions
    - 0: vectors are perpendicular
    - -1: vectors point in opposite directions
- **Best for**: When you only care about how parallel vectors are, regardless of their size

#### When to Use Each

- **Use dot product when**: You need to account for both how aligned vectors are AND how large they are
    - Physics calculations (work, force projections)
    - When magnitude matters as much as direction

- **Use cosine similarity when**: You only care about similarity in direction, regardless of size
    - Text analysis (comparing documents regardless of length)
    - Recommendation systems (comparing preferences regardless of intensity)
    - Pattern recognition (when scale shouldn't affect similarity)


### Properties

- **Commutative**: $\mathbf{u} \cdot \mathbf{v} = \mathbf{v} \cdot \mathbf{u}$
- **Distributive**: $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$
- **Scalar Multiplication**: $(a\mathbf{u}) \cdot \mathbf{v} = a(\mathbf{u} \cdot \mathbf{v})$
- **Zero Vector**: If $\mathbf{u} = \mathbf{0}$ or $\mathbf{v} = \mathbf{0}$, then $\mathbf{u} \cdot \mathbf{v} = 0$
- **Perpendicular Vectors**: If $\mathbf{u} \cdot \mathbf{v} = 0$ and neither vector is zero, then $\mathbf{u}$ and $\mathbf{v}$ are perpendicular

### Applications

- **Work in Physics**: When a force moves an object, the work done is the dot product of force and displacement
- **Projection**: Finding how much of one vector lies in the direction of another
- **Orthogonality Testing**: Checking if vectors are perpendicular
- **Machine Learning**: Computing similarity between vectors in vector spaces

### Implementation Considerations

- Both vectors must have the same dimension
- The operation has linear time complexity O(n), where n is the dimension of the vectors
- Handle edge cases like zero vectors appropriately

# Ex 04

## Norm (Vector Length)

The norm of a vector, also called magnitude or length, measures the "size" of a vector. There are several types of norms, each with specific applications.

### Types of Norms

#### L1 Norm (Manhattan Norm)

The L1 norm sums the absolute values of the vector components:

$$
||\mathbf{v}||_1 = |v_1| + |v_2| + ... + |v_n| = \sum_{i=1}^{n} |v_i|
$$

#### L2 Norm (Euclidean Norm)

The L2 norm is the most common and represents the straight-line distance:

$$
||\mathbf{v}||_2 = \sqrt{v_1^2 + v_2^2 + ... + v_n^2} = \sqrt{\sum_{i=1}^{n} v_i^2}
$$

This is equivalent to $\sqrt{\mathbf{v} \cdot \mathbf{v}}$

#### Infinity Norm (Max Norm)

The infinity norm takes the largest absolute value among components:

$$
||\mathbf{v}||_{\infty} = \max(|v_1|, |v_2|, ..., |v_n|)
$$

### Example Calculations

For vector $\mathbf{v} = [3, -4, 5]$:

- **L1 Norm**: $||\mathbf{v}||_1 = |3| + |-4| + |5| = 3 + 4 + 5 = 12$
- **L2 Norm**: $||\mathbf{v}||_2 = \sqrt{3^2 + (-4)^2 + 5^2} = \sqrt{9 + 16 + 25} = \sqrt{50} \approx 7.07$
- **Infinity Norm**: $||\mathbf{v}||_{\infty} = \max(|3|, |-4|, |5|) = 5$

### Visual Representation

<details>
    <summary><b>Click to view Vector Norms Comparison</b></summary>
    <img src="./assets/vector_norms.png" alt="Different Vector Norms" width="50%" height="50%" />
    <p><i>Different norms measure vector length in different ways. The colored shapes show unit circles in each norm.</i></p>
</details>

### Properties

- **Non-negativity**: $||\mathbf{v}|| \geq 0$ for any vector $\mathbf{v}$
- **Zero Vector**: $||\mathbf{v}|| = 0$ if and only if $\mathbf{v} = \mathbf{0}$
- **Scalar Multiplication**: $||a\mathbf{v}|| = |a| \times ||\mathbf{v}||$
- **Triangle Inequality**: $||\mathbf{u} + \mathbf{v}|| \leq ||\mathbf{u}|| + ||\mathbf{v}||$

### Applications

- **Machine Learning**: Norms play crucial roles in:
    - **Regularization**: L1 norm (Lasso) promotes sparsity by forcing some weights to zero; L2 norm (Ridge) prevents overfitting by keeping weights small
    ---
    - **L1 Loss (Mean Absolute Error)**: More robust to outliers, creates sparse solutions
        - Formula: $L1 = \sum_{i=1}^{n}|y_i - \hat{y}_i|$
                    <details>
                        <summary><b>Click to see L1 Loss Example</b></summary>
                        <h3>L1 Loss (Mean Absolute Error) Example</h3>
                        <p>Let's illustrate L1 loss with a simple example:</p>
                        <p>Imagine you're building a model to predict house prices:</p>
                        <pre>
    Actual house prices (in $1000s): [200, 250, 300, 700]
    Your model predicts: [210, 230, 320, 450]
                        </pre>
                        <p>The L1 loss calculation would be:</p>
                        <pre>
    L1 = |200-210| + |250-230| + |300-320| + |700-450|
        = 10 + 20 + 20 + 250
        = 300
                        </pre>
            <p>Each error contributes exactly its absolute difference to the total loss. Note how the large error on the last house (250) doesn't dominate the calculation - it's just added linearly. In contrast, with L2 loss, that 250 error would be squared (62500), causing it to overwhelmingly dominate the total loss.</p>
            <p>This is why L1 loss is more robust to outliers - the last house might be an unusual mansion, but it won't cause your model to sacrifice accuracy on typical homes just to reduce that one large error.</p>
    - **L2 Loss (Mean Squared Error)**: Heavily penalizes large errors, has smooth gradients, computationally efficient
        - Formula: $L2 = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2$
                    <details>
                        <summary><b>Click to see L2 Loss Example</b></summary>
                        <h3>L2 Loss (Mean Squared Error) Example</h3>
                        <p>Let's illustrate L2 loss with the same house price prediction example:</p>
                        <pre>
    Actual house prices (in $1000s): [200, 250, 300, 700]
    Your model predicts: [210, 230, 320, 450]
                        </pre>
                        <p>The L2 loss calculation would be:</p>
                        <pre>
    L2 = (200-210)² + (250-230)² + (300-320)² + (700-450)²
        = 100 + 400 + 400 + 62500
        = 63400
                        </pre>
                        <p>Notice how the last error (250) when squared becomes 62500, completely dominating the total loss. This single outlier accounts for over 98% of your total L2 loss!</p>
                        <p>This demonstrates why L2 loss is more sensitive to outliers - the model will prioritize reducing large errors even if it means making the predictions for other houses slightly worse. The benefit is that the L2 loss has smoother gradients (helpful for optimization algorithms) and often leads to models with better overall accuracy when outliers aren't a concern.</p>
                    </details>
    ---
    - **Feature Normalization**: Scaling features using specific norms:
        - **L2 normalization**: Ensures all samples have unit Euclidean length, preserves direction

            <details>
            <summary><b>Click to see L2 Normalization Example</b></summary>
            <h3>L2 Normalization Explained</h3>
            <p>L2 normalization (also called Euclidean normalization) is a technique that scales each sample vector so that its L2 norm (Euclidean length) equals 1.</p>
            
            <h4>What it does</h4>
            <p>L2 normalization transforms a vector <code>x</code> into a unit vector that points in the same direction:</p>
            
            <pre>x_normalized = x / ||x||₂</pre>
            
            <p>Where <code>||x||₂</code> is the L2-norm (Euclidean norm) calculated as:</p>
            
            <pre>||x||₂ = sqrt(x₁² + x₂² + ... + xₙ²)</pre>
            
            <h4>Key properties</h4>
            <ol>
            <li><strong>Preserves direction</strong>: The normalized vector points in the same direction as the original vector</li>
            <li><strong>Unit length</strong>: All normalized vectors have a length of 1</li>
            <li><strong>Scale invariance</strong>: Only the direction of the data matters, not its magnitude</li>
            <li><strong>Removes magnitude differences</strong>: Helpful when features have different scales</li>
            </ol>
            
            <h4>When to use it</h4>
            <ul>
            <li><strong>Text analysis</strong>: In TF-IDF vectors to focus on relative word importance</li>
            <li><strong>Image processing</strong>: When comparing image features</li>
            <li><strong>Machine learning</strong>: When you want algorithms to focus on the direction of data points rather than their magnitude</li>
            <li><strong>Similarity measures</strong>: Particularly for cosine similarity calculations</li>
            </ul>
            
            <h4>Example</h4>
                <pre>
                    # Original vector: [4, 3]
                    # L2 norm = sqrt(4² + 3²) = sqrt(16 + 9) = sqrt(25) = 5
                    # Normalized vector = [4/5, 3/5] = [0.8, 0.6]
                </pre>
            <p>After normalization, all vectors will lie on the unit sphere, making them suitable for algorithms that rely on directional relationships.</p>
            </details>
    ---
    - **Gradient-Based Learning**: Computing gradient norms to monitor convergence in optimization algorithms
- **Optimization**: Defining objective functions and constraints

### Implementation Notes

- For the L2 norm, be careful about numerical overflow with large values
- The choice of norm depends on the application context
- Time complexity is O(n) for all norm calculations, where n is the vector dimension

# Ex 05

## Cosine Similarity


### In Simple Terms

<span style="color:red">**The goal of cosine similarity** </span>is to determine if two items are pointing in the same direction, regardless of their magnitude. It helps answer: "Are these two items similar in their orientation?" - like checking if two people have similar preferences even if one rates everything more intensely than the other.

### Definition

Cosine similarity measures the cosine of the angle between two non-zero vectors in an inner product space.

### Definition

The cosine similarity between two vectors $\mathbf{u}$ and $\mathbf{v}$ is calculated using their dot product and magnitudes:

$$
\text{Cosine Similarity}(\mathbf{u}, \mathbf{v}) = \cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{||\mathbf{u}|| \times ||\mathbf{v}||}
$$

Where:
- $\mathbf{u} \cdot \mathbf{v}$ is the dot product of vectors $\mathbf{u}$ and $\mathbf{v}$.
- $||\mathbf{u}||$ and $||\mathbf{v}||$ are the L2 norms (magnitudes) of vectors $\mathbf{u}$ and $\mathbf{v}$.
- $\theta$ is the angle between the two vectors.

### Interpretation

The value of cosine similarity ranges from -1 to 1:
- **1**: The vectors point in the exact same direction (angle is 0°). They are maximally similar.
- **0**: The vectors are orthogonal (perpendicular, angle is 90°). They have no similarity in terms of direction.
- **-1**: The vectors point in opposite directions (angle is 180°). They are maximally dissimilar.

Cosine similarity focuses on the orientation (direction) of the vectors, not their magnitude.

### Example Calculation

Let $\mathbf{u} = [2, 1]$ and $\mathbf{v} = [3, 4]$.

1.  **Calculate the dot product**:
    $$
    \mathbf{u} \cdot \mathbf{v} = (2 \times 3) + (1 \times 4) = 6 + 4 = 10
    $$
2.  **Calculate the magnitudes**:
    $$
    ||\mathbf{u}|| = \sqrt{2^2 + 1^2} = \sqrt{4 + 1} = \sqrt{5}
    $$
    $$
    ||\mathbf{v}|| = \sqrt{3^2 + 4^2} = \sqrt{9 + 16} = \sqrt{25} = 5
    $$
3.  **Calculate the cosine similarity**:
    $$
    \cos(\theta) = \frac{10}{\sqrt{5} \times 5} = \frac{10}{5\sqrt{5}} = \frac{2}{\sqrt{5}} = \frac{2\sqrt{5}}{5} \approx 0.894
    $$
The cosine similarity is approximately 0.894, indicating that the vectors point in roughly the same direction.

### Visual Representation

<details>
    <summary><b>Click to view Cosine Similarity Visualization</b></summary>
    <img src="./assets/cosine_similarity.png" alt="Cosine Similarity" width="60%" height="60%" />
    <p><i>Cosine similarity measures the angle θ between two vectors. Vectors pointing in similar directions have a cosine similarity close to 1. Orthogonal vectors have a similarity of 0. Vectors pointing in opposite directions have a similarity close to -1.</i></p>
</details>

### Applications

- **Text Analysis / Natural Language Processing (NLP)**: Measuring similarity between documents represented as vectors (e.g., TF-IDF vectors). Documents with similar content tend to have vectors pointing in similar directions.
- **Recommendation Systems**: Finding users or items with similar preferences based on their vector representations.
- **Information Retrieval**: Ranking documents based on their similarity to a query vector.
- **Bioinformatics**: Comparing gene expression data.

### Implementation Considerations

- Both vectors must have the same dimension.
- Handle the case where one or both vectors are zero vectors (magnitude is zero), which would lead to division by zero. Cosine similarity is typically undefined or considered 0 in this case, depending on the context.
- The complexity is dominated by the dot product and norm calculations, typically O(n) where n is the vector dimension.

# Ex 06

## The Cross Product

The cross product is an operation between two vectors in three-dimensional space that results in a third vector, which is perpendicular(Means) to both of the original vectors.

**<span style="color:red">Perpendicular means</span>**:
(meaning they meet at a right angle, like the corner of a square).

### Definition

For two vectors in 3D space, $\mathbf{u} = [u_1, u_2, u_3]$ and $\mathbf{v} = [v_1, v_2, v_3]$, their cross product $\mathbf{u} \times \mathbf{v}$ is defined as:

$$
\mathbf{u} \times \mathbf{v} = [u_2 v_3 - u_3 v_2, \,\, u_3 v_1 - u_1 v_3, \,\, u_1 v_2 - u_2 v_1]
$$


### Determinant Calculation Method

<details>
    <summary><b>Click to view Cross Product Calculation Step by Step</b></summary>
    
When using the determinant method to calculate the cross product, you can follow these steps:

1. Set up the determinant:
   
   $$
   \mathbf{u} \times \mathbf{v} = \begin{vmatrix}
   \mathbf{i} & \mathbf{j} & \mathbf{k} \\
   u_1 & u_2 & u_3 \\
   v_1 & v_2 & v_3 \\
   \end{vmatrix}
   $$

2. Calculate each component using the minors of the first row:

   ![Cross Product Calculation](./assets/CalculateCrossProduct.png)

3. This gives you the resulting vector:
   
   $$
   \mathbf{u} \times \mathbf{v} = \begin{pmatrix}
   u_2v_3 - u_3v_2 \\
   u_3v_1 - u_1v_3 \\
   u_1v_2 - u_2v_1
   \end{pmatrix}
   $$

</details>

### Geometric Interpretation

-   **Direction**: The resulting vector $\mathbf{u} \times \mathbf{v}$ is orthogonal (perpendicular) to both $\mathbf{u}$ and $\mathbf{v}$. Its direction is determined by the right-hand rule.
-   **Magnitude**: The magnitude of the cross product is related to the angle $\theta$ between the vectors:
    $$
    ||\mathbf{u} \times \mathbf{v}|| = ||\mathbf{u}|| \times ||\mathbf{v}|| \times |\sin(\theta)|
    $$
    This magnitude is equal to the area of the parallelogram spanned by the vectors $\mathbf{u}$ and $\mathbf{v}$.

[Click here to view the 3D Geometric Representation Online](https://www.desmos.com/3d/ag0twyzjye?lang=fr)

### Example Calculation

Let $\mathbf{u} = [1, 2, 3]$ and $\mathbf{v} = [3, 4, 5]$.

Using the formula:
$$
\begin{aligned}
\mathbf{u} \times \mathbf{v} &= [(u_2 v_3 - u_3 v_2), (u_3 v_1 - u_1 v_3), (u_1 v_2 - u_2 v_1)] \\
&= [(2 \times 5 - 3 \times 4), (3 \times 3 - 1 \times 5), (1 \times 4 - 2 \times 3)] \\
&= [10 - 12, 9 - 5, 4 - 6] \\
&= [-2, 4, -2]
\end{aligned}
$$
The resulting vector $[-2, 4, -2]$ is perpendicular to both $[1, 2, 3]$ and $[3, 4, 5]$.

To verify, we can check the dot products:
$$
[-2, 4, -2] \cdot [1, 2, 3] = (-2 \times 1) + (4 \times 2) + (-2 \times 3) = -2 + 8 - 6 = 0
$$
$$
[-2, 4, -2] \cdot [3, 4, 5] = (-2 \times 3) + (4 \times 4) + (-2 \times 5) = -6 + 16 - 10 = 0
$$
Since the dot products are zero, the resulting vector is indeed orthogonal to both $\mathbf{u}$ and $\mathbf{v}$.

### Properties

-   **Anti-commutative**: $\mathbf{u} \times \mathbf{v} = -(\mathbf{v} \times \mathbf{u})$
-   **Distributive over addition**: $\mathbf{u} \times (\mathbf{v} + \mathbf{w}) = (\mathbf{u} \times \mathbf{v}) + (\mathbf{u} \times \mathbf{w})$
-   **Scalar Multiplication**: $(a\mathbf{u}) \times \mathbf{v} = \mathbf{u} \times (a\mathbf{v}) = a(\mathbf{u} \times \mathbf{v})$
-   **Not Associative**: $(\mathbf{u} \times \mathbf{v}) \times \mathbf{w} \neq \mathbf{u} \times (\mathbf{v} \times \mathbf{w})$
-   **Zero Vector**: $\mathbf{u} \times \mathbf{u} = \mathbf{0}$ (The cross product of a vector with itself is the zero vector).
-   **Parallel Vectors**: If $\mathbf{u}$ and $\mathbf{v}$ are parallel ($\theta = 0^\circ$ or $180^\circ$), then $\mathbf{u} \times \mathbf{v} = \mathbf{0}$.

### Applications

-   **Physics**: Calculating torque, angular momentum, and the force on a moving charge in a magnetic field (Lorentz force).
-   **Computer Graphics**: Finding the normal vector to a surface (e.g., a triangle in a 3D model), which is crucial for lighting calculations.
-   **Geometry**: Determining if points are collinear, finding the area of a triangle or parallelogram in 3D space, finding a vector perpendicular to a plane defined by two vectors.

### Implementation Considerations

-   The cross product is only defined for vectors in 3-dimensional space.
-   The calculation involves a fixed number of multiplications and subtractions, so its time complexity is O(1).
-   Ensure correct implementation of the formula or determinant calculation to get the right components and signs.

---

# Ex 07

## Matrix Multiplication

Matrix multiplication is a fundamental operation where two matrices are combined to produce a third matrix. Unlike element-wise addition or subtraction, matrix multiplication involves multiplying rows of the first matrix by columns of the second matrix.

### Definition

If $A$ is an $m \times n$ matrix and $B$ is an $n \times p$ matrix, their product $C = AB$ is an $m \times p$ matrix. The entry $C_{ij}$ (in the $i$-th row and $j$-th column of $C$) is calculated by taking the dot product of the $i$-th row of $A$ and the $j$-th column of $B$.

### Compatibility Requirement

For matrix multiplication to be defined, the matrices must have compatible dimensions:

- If matrix $A$ is of size $m \times n$ (m rows, n columns)
- And matrix $B$ is of size $n \times p$ (n rows, p columns)
- Then the product $C = AB$ is defined and will be of size $m \times p$

**Key points about compatibility:**

- The number of columns in the first matrix must equal the number of rows in the second matrix
- If this condition isn't met, the multiplication is undefined
- The resulting matrix will have the same number of rows as the first matrix and the same number of columns as the second matrix

**Matrix-Vector Multiplication:**

When multiplying a matrix by a vector:
- A vector can be treated as an $n \times 1$ matrix (a column vector)
- If matrix $A$ is of size $m \times n$ and vector $\mathbf{v}$ is of size $n \times 1$
- Then the product $A\mathbf{v}$ is defined and will be a vector of size $m \times 1$
- Each element of the resulting vector is the dot product of a row from $A$ with the vector $\mathbf{v}$

**Visual representation of compatible dimensions:**

```
A (m×n) × B (n×p) = C (m×p)
A (m×n) × v (n×1) = w (m×1)
```

**Example of compatible matrices:**
- A 3×5 matrix can be multiplied by a 5×2 matrix, resulting in a 3×2 matrix
- A 2×2 matrix can be multiplied by a 2×3 matrix, resulting in a 2×3 matrix
- A 4×3 matrix can be multiplied by a 3×1 vector, resulting in a 4×1 vector

**Example of incompatible matrices:**
- A 2×3 matrix cannot be multiplied by a 2×2 matrix (3 ≠ 2)
- A 4×1 matrix cannot be multiplied by a 3×5 matrix (1 ≠ 3)
- A 2×3 matrix cannot be multiplied by a 4×1 vector (3 ≠ 4)

### Formula

The element $C_{ij}$ of the product matrix $C = AB$ is given by:

$$
C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
$$

This means you multiply corresponding elements from the $i$-th row of $A$ and the $j$-th column of $B$ and sum the results.

### Example Calculation

Let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ (a 2x2 matrix) and $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$ (a 2x2 matrix).

The product $C = AB$ will be a 2x2 matrix.

-   **Element $C_{11}$**: (Row 1 of A) $\cdot$ (Column 1 of B)
    $$ C_{11} = (1 \times 5) + (2 \times 7) = 5 + 14 = 19 $$
-   **Element $C_{12}$**: (Row 1 of A) $\cdot$ (Column 2 of B)
    $$ C_{12} = (1 \times 6) + (2 \times 8) = 6 + 16 = 22 $$
-   **Element $C_{21}$**: (Row 2 of A) $\cdot$ (Column 1 of B)
    $$ C_{21} = (3 \times 5) + (4 \times 7) = 15 + 28 = 43 $$
-   **Element $C_{22}$**: (Row 2 of A) $\cdot$ (Column 2 of B)
    $$ C_{22} = (3 \times 6) + (4 \times 8) = 18 + 32 = 50 $$

So, the resulting matrix is:
$$
C = AB = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}
$$

### Matrix-Vector Example

Let $M = \begin{pmatrix} 2 & 3 & 4 \\ 1 & 0 & 5 \end{pmatrix}$ (a 2x3 matrix) and $\mathbf{v} = \begin{pmatrix} 6 \\ 7 \\ 8 \end{pmatrix}$ (a 3x1 vector).

The product $M\mathbf{v}$ will be a 2x1 vector.

-   **First element**: (Row 1 of M) $\cdot$ $\mathbf{v}$
    $$ (M\mathbf{v})_1 = (2 \times 6) + (3 \times 7) + (4 \times 8) = 12 + 21 + 32 = 65 $$
-   **Second element**: (Row 2 of M) $\cdot$ $\mathbf{v}$
    $$ (M\mathbf{v})_2 = (1 \times 6) + (0 \times 7) + (5 \times 8) = 6 + 0 + 40 = 46 $$

So, the resulting vector is:
$$
M\mathbf{v} = \begin{pmatrix} 65 \\ 46 \end{pmatrix}
$$


### Properties

-   **Not Commutative**: In general, $AB \neq BA$. The order of multiplication matters. $BA$ might not even be defined if the dimensions don't match correctly.
-   **Associative**: $(AB)C = A(BC)$, provided the dimensions are compatible for all multiplications.
-   **Distributive**:
    -   $A(B + C) = AB + AC$ (Left distributivity)
    -   $(A + B)C = AC + BC$ (Right distributivity)
-   **Identity Matrix**: If $I$ is the identity matrix of appropriate size, then $AI = A$ and $IA = A$.
-   **Scalar Multiplication**: $(kA)B = A(kB) = k(AB)$, where $k$ is a scalar.

### Applications

-   **Linear Transformations**: Representing sequences of transformations (like rotation followed by scaling) as a single matrix.
-   **Solving Systems of Linear Equations**: Used in methods like Gaussian elimination and matrix inversion.
-   **Computer Graphics**: Transforming points and vectors (translation, rotation, scaling, projection).
-   **Graph Theory**: Finding paths of a certain length in adjacency matrices.
-   **Physics and Engineering**: Modeling systems, simulations, quantum mechanics.
-   **Machine Learning**: Neural network layers, principal component analysis (PCA).

### Implementation Considerations

-   Always check if the matrices are compatible for multiplication (inner dimensions must match).
-   The standard algorithm has a time complexity of $O(m \times n \times p)$ for multiplying an $m \times n$ matrix by an $n \times p$ matrix. More advanced algorithms like Strassen's algorithm exist but are typically practical only for very large matrices.
-   Numerical stability can be a concern with floating-point numbers.

# Ex 08

## Trace

The trace of a square matrix is the sum of the elements on its main diagonal (from the upper left to the lower right).

### Definition

For an $n \times n$ square matrix $A$, the trace, denoted as $\text{tr}(A)$, is defined as:

$$
\text{tr}(A) = \sum_{i=1}^{n} A_{ii} = A_{11} + A_{22} + \dots + A_{nn}
$$

Where $A_{ii}$ represents the element in the $i$-th row and $i$-th column of matrix $A$.

### Compatibility Requirement

-   The trace operation is only defined for **square matrices** (matrices with the same number of rows and columns, i.e., $n \times n$).

### Example Calculation

Let $A$ be a 3x3 matrix:
$$
A = \begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix}
$$

The main diagonal elements are $A_{11} = 1$, $A_{22} = 5$, and $A_{33} = 9$.

The trace of $A$ is:
$$
\text{tr}(A) = 1 + 5 + 9 = 15
$$

Another example with a 2x2 matrix:
$$
B = \begin{pmatrix}
-2 & 0 \\
 3 & 7
\end{pmatrix}
$$
The trace of $B$ is:
$$
\text{tr}(B) = -2 + 7 = 5
$$

### Properties

Let $A$ and $B$ be $n \times n$ square matrices and $c$ be a scalar.

-   **Linearity**:
    -   $\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$
    -   $\text{tr}(cA) = c \times \text{tr}(A)$
-   **Transpose Invariance**: $\text{tr}(A) = \text{tr}(A^T)$, where $A^T$ is the transpose of $A$.
-   **Cyclic Property**: $\text{tr}(ABC) = \text{tr}(BCA) = \text{tr}(CAB)$ (for compatible matrices $A, B, C$). This implies $\text{tr}(AB) = \text{tr}(BA)$ even if $AB \neq BA$.
-   **Trace and Eigenvalues**: The trace of a matrix is equal to the sum of its eigenvalues (counting multiplicities).
-   **Trace of Identity Matrix**: $\text{tr}(I_n) = n$, where $I_n$ is the $n \times n$ identity matrix.

### Applications

-   **Linear Algebra**: Used in defining matrix norms (like the Frobenius norm), studying eigenvalues, and characterizing linear transformations.
-   **Physics**: Appears in quantum mechanics and statistical mechanics (e.g., partition functions).
-   **Differential Geometry**: Used in defining curvature.
-   **Machine Learning**: Appears in various contexts, including optimization algorithms and analysis of covariance matrices. For example, the trace of the covariance matrix represents the total variance in the data.
-   **Numerical Analysis**: Used in matrix decomposition methods and stability analysis.

### Implementation Considerations

-   Ensure the input matrix is square before attempting to calculate the trace.
-   The calculation involves summing $n$ elements, so the time complexity is $O(n)$, where $n$ is the dimension of the square matrix.
-   It's a straightforward operation, generally numerically stable.
# Ex 09

## Transpose

The transpose of a matrix is an operation that flips the matrix over its main diagonal, effectively swapping the row and column indices.

### Definition

For an $m \times n$ matrix $A$, its transpose, denoted as $A^T$, is an $n \times m$ matrix where the element in the $i$-th row and $j$-th column of $A^T$ is the element from the $j$-th row and $i$-th column of $A$.

$$
(A^T)_{ij} = A_{ji}
$$

In simpler terms, the rows of $A$ become the columns of $A^T$, and the columns of $A$ become the rows of $A^T$.

### Compatibility Requirement

-   The transpose operation can be applied to **any matrix**, regardless of its dimensions (it does not need to be square). If $A$ is $m \times n$, then $A^T$ is $n \times m$.

### Example Calculation

Let $A$ be a 3x2 matrix:
$$
A = \begin{pmatrix}
1 & 2 \\
3 & 4 \\
5 & 6
\end{pmatrix}
$$

To find its transpose $A^T$, we swap rows and columns:
-   The first row $[1, 2]$ becomes the first column.
-   The second row $[3, 4]$ becomes the second column.
-   The third row $[5, 6]$ becomes the third column.

The transpose $A^T$ is a 2x3 matrix:
$$
A^T = \begin{pmatrix}
1 & 3 & 5 \\
2 & 4 & 6
\end{pmatrix}
$$

### Properties

Let $A$ and $B$ be matrices of compatible dimensions and $c$ be a scalar.

-   **Involution**: $(A^T)^T = A$ (Transposing twice returns the original matrix).
-   **Additivity**: $(A + B)^T = A^T + B^T$ (The transpose of a sum is the sum of the transposes).
-   **Scalar Multiplication**: $(cA)^T = c A^T$ (The transpose of a scaled matrix is the scalar times the transposed matrix).
-   **Product Rule**: $(AB)^T = B^T A^T$ (The transpose of a product is the product of the transposes in reverse order).
-   **Determinant**: $\det(A^T) = \det(A)$ (The determinant of the transpose is the same as the original, only for square matrices).
-   **Trace**: $\text{tr}(A^T) = \text{tr}(A)$ (The trace is invariant under transposition, only for square matrices).

### Applications

-   **Linear Algebra**: Solving systems of linear equations (e.g., normal equations $A^T A x = A^T b$), defining orthogonal matrices ($A^T A = I$), calculating covariance matrices in statistics.
-   **Data Science / Machine Learning**: Reshaping data, calculating gradients in optimization, defining certain types of neural network layers.
-   **Computer Graphics**: Sometimes used in transformation calculations, especially involving normal vectors.
-   **Numerical Analysis**: Used in various matrix factorization algorithms (like QR decomposition).

### Implementation Considerations

-   The transpose operation typically involves creating a new matrix with swapped dimensions.
-   The time complexity is $O(m \times n)$, as each element of the original matrix needs to be accessed and placed into the new matrix.
-   For square matrices, in-place transposition is possible but more complex to implement correctly.
# Ex 10

## Row Echelon Form

Row Echelon Form (REF) is a way of organizing a matrix to reveal key properties such as its rank and pivot structure. Below are the core rules and examples to illustrate the concept.


### Elementary Row Operations

There are three types of elementary row operations:

1.  **Swapping:** Interchange two rows ($R_i \leftrightarrow R_j$).
2.  **Scaling:** Multiply a row by a non-zero scalar ($R_i \rightarrow c R_i$, where $c \neq 0$).
3.  **Replacement:** Add a multiple of one row to another row ($R_i \rightarrow R_i + k R_j$, where $k$ is any scalar and $i \neq j$).

<details>
<summary><span style="color:red">Click to view notation explanation</span></summary>

Okay, let's break down the notation used for each elementary row operation:

1.  **Swapping: $R_i \leftrightarrow R_j$**
    *   `R`: Stands for "Row".
    *   `i`, `j`: These are subscripts representing the *indices* or *numbers* of the rows you are working with. For example, `R₁` would be the first row, `R₂` the second, and so on. `i` and `j` are just placeholders for specific row numbers.
    *   `↔`: This double-headed arrow signifies an *interchange* or *swap*. It means row `i` and row `j` exchange places.

2.  **Scaling: $R_i \rightarrow c R_i$, where $c \neq 0$**
    *   `R`: Stands for "Row".
    *   `i`: The index of the row being modified.
    *   `→`: This arrow means "is replaced by" or "becomes". It indicates the result of the operation.
    *   `c`: Represents a *scalar*, which is just a constant number (like 2, -5, or 0.5).
    *   `c R_i`: This means you multiply *every element* in row `i` by the scalar `c`.
    *   `c ≠ 0`: This is a condition stating that the scalar `c` *must not be zero*. You can't multiply a row by zero because that would lose information and make the operation irreversible.

3.  **Replacement: $R_i \rightarrow R_i + k R_j$, where $k$ is any scalar and $i \neq j$**
    *   `R`: Stands for "Row".
    *   `i`, `j`: Indices for the rows involved. `Rᵢ` is the row being *replaced*, and `Rⱼ` is the row being *used* to modify `Rᵢ`.
    *   `→`: Means "is replaced by".
    *   `k`: Represents any scalar (it *can* be zero in this case).
    *   `k R_j`: This means you first multiply every element in row `j` by the scalar `k`.
    *   `R_i + k R_j`: This signifies adding the corresponding elements of the *original* row `i` and the *scaled* row `j` (`k R_j`). The result of this addition becomes the *new* row `i`.
    *   `i ≠ j`: This condition states that the row being replaced (`i`) must be different from the row being used to perform the replacement (`j`). You add a multiple of *another* row to the target row.

</details>

### Criteria for Row Echelon Form (REF)

A matrix is in Row Echelon Form if it meets these conditions:

1.  **Zero Rows:** All rows consisting entirely of zeros are grouped at the bottom of the matrix.
2.  **Leading Entries (Pivots):** For each non-zero row, the first non-zero entry (called the leading entry or pivot) is strictly to the right of the leading entry of the row above it.


### Example (Correct REF)

```text
[ 2  5  3 ]
[ 0 -2  5 ]
[ 0  0  0 ]

Pivot positions (●):
[ ● - - ]
[ - ● - ]
[ - - ● ]
```

This clearly shows the staircase pattern of the pivots stepping to the right as you move down:

- Row 1 pivot at column 1
- Row 2 pivot at column 2
- Row 3 is all zeros (no pivot)

---

This matrix follows the rules:

- All-zero row is at the bottom.
- Pivots are at (1,1) and (2,2), forming a clear staircase.

---

### Example (Incorrect REF)

```text
[ 1  2  3  4 ]
[ 0  0  1  2 ]
[ 0  0  1  0 ]
[ 0  0  0  2 ]

Pivot positions (●):
[●  -  -  -]
[ -  -  ●  -]
[ -  -  ●  -]
[ -  -  -  ●]
```

> *This matrix does ****************not**************** follow the staircase pattern* — notice the pivot in row 3 (column 3) does not step to the right of the pivot in row 2.

> *This matrix does ********************not******************** follow the staircase pattern* — the third row's pivot (at column 3) does not move strictly to the right of the second row's pivot.

---

## 2. Why REF Matters

- **Pivots** are the first non-zero entries in each non-zero row.
- **Pivot columns** are the columns containing these pivots.
- The **rank** of the matrix (dimension of the row space or column space) equals the number of pivots.

### Example (Computing Rank)

$$
\begin{pmatrix}
4 & 2 & 9 & 1 \\
0 & 0 & 3 & 2 \\
0 & 0 & 0 & 2 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$
<details>
<summary><b><span style="color:red">Click to view REF Fundamentals Visualization</span></b></summary>
<img src="./assets/fundamentals_Row_echelon.png" alt="Row Echelon Form Fundamentals" width="70%" height="70%" />
<p><i>This image illustrates the key concepts: pivots (leading non-zero entries), pivot columns, and how the number of pivots determines the rank.</i></p>
</details>
> Here, there are 3 pivots (in columns 1, 3, and 4), so

**Rank = 3.**

---

*End of REF summary.*



*(Note: Some definitions require pivots to be 1, but often this is reserved for Reduced Row Echelon Form).*

### Example Calculation (Gaussian Elimination to REF)

Let's transform the following matrix into Row Echelon Form:
$$
A = \begin{pmatrix}
1 & 2 & 3 \\
2 & 5 & 8 \\
1 & 1 & 2
\end{pmatrix}
$$

1.  **Eliminate entries below the first pivot (A<sub>11</sub>=1):**
    *   Replace $R_2$ with $R_2 - 2R_1$:
        $$ \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 1 & 1 & 2 \end{pmatrix} $$
    *   Replace $R_3$ with $R_3 - R_1$:
        $$ \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & -1 & -1 \end{pmatrix} $$
2.  **Eliminate entries below the second pivot (A<sub>22</sub>=1):**
    *   Replace $R_3$ with $R_3 + R_2$:
        $$ \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix} $$

The resulting matrix is now in Row Echelon Form:
$$
A_{REF} = \begin{pmatrix}
1 & 2 & 3 \\
0 & 1 & 2 \\
0 & 0 & 1
\end{pmatrix}
$$
It satisfies the conditions: no zero rows, and the leading entries (1, 1, 1) move progressively to the right.

### Reduced Row Echelon Form (RREF)

A matrix is in **Reduced Row Echelon Form (RREF)** if it meets the REF conditions plus two more:

1.  **Pivot Value:** Every leading entry (pivot) is 1.
2.  **Zeroes Above Pivots:** Each leading 1 is the only non-zero entry in its column.

Continuing the example to get RREF:
$$
A_{REF} = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 2 \\ 0 & 0 & 1 \end{pmatrix}
$$
1.  **Eliminate entries above the third pivot (A<sub>33</sub>=1):**
    *   $R_2 \rightarrow R_2 - 2R_3$:
        $$ \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
    *   $R_1 \rightarrow R_1 - 3R_3$:
        $$ \begin{pmatrix} 1 & 2 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$
2.  **Eliminate entries above the second pivot (A<sub>22</sub>=1):**
    *   $R_1 \rightarrow R_1 - 2R_2$:
        $$ \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix} $$

The resulting matrix is the identity matrix, which is in RREF.
$$
A_{RREF} = \begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{pmatrix}
$$

<details>
<summary><b><span style="color:red">Click to view RREF Example Details</span></b></summary>
<img src="./assets/reducedRowEchelonFormDetailed.png" alt="RREF Detailed Example" width="70%" height="70%" />
<p><i>This image shows the step-by-step transformation of a matrix into Reduced Row Echelon Form (RREF), highlighting the row operations used.</i></p>
</details>

<details>
<summary><b><span style="color:blue">Click to view Python Function Explanation (Gauss-Jordan Elimination)</span></b></summary>

---

## Elementary Row Operations in Gauss–Jordan Elimination

In the `row_echelon` method of the `Matrix` class, the three classic **elementary row operations** are applied to transform the matrix into its **reduced row-echelon form** (RREF). Below is a detailed explanation in **Markdown** with **LaTeX** formulas.

---

### 1. Row Swapping

When there is no nonzero pivot in the current row, the algorithm searches the rows below and, if it finds one, swaps rows:

```python
# Code:
A[pivot_row], A[pivot] = A[pivot], A[pivot_row]
```

**LaTeX formula**:

$$
R_{i} \longleftrightarrow R_{j}
$$

- *Description*: Swap row $R_i$ with row $R_j$.

---

### 2. Row Scaling (Normalization)

Once the pivot row is in place, the entire row is divided by the pivot value to make the pivot element equal to 1:

```python
pv = A[pivot_row][col]
A[pivot_row] = [x / pv for x in A[pivot_row]]
```

**LaTeX formula**:

$$
R_i := \frac{1}{a_{ii}}\,R_i
$$

- *Description*: Multiply row $R_i$ by the scalar $\frac{1}{a_{ii}}$, where $a_{ii}$ is the pivot element.

---

### 3. Row Replacement (Elimination)

To eliminate all other entries in the pivot column, subtract an appropriate multiple of the pivot row from each other row:

```python
factor = A[r][col]
A[r] = [a_r - factor * a_p for a_r, a_p in zip(A[r], A[pivot_row])]
```

**LaTeX formula**:

$$
R_j := R_j - \ell\,R_i
$$

- *Description*: Subtract $\ell = R_j[\text{col}]$ times the pivot row $R_i$ from row $R_j$ to zero out the pivot column entry.

---

### Full Algorithm Flow

1. Iterate over each column $j = 0, 1, \dots, n-1$ while there are unprocessed rows.
2. Find a nonzero pivot in or below the current pivot row.
3. **Row swapping** if the pivot is not already in the pivot row.
4. **Row scaling** to make the pivot element $1$ at position $(i, j)$.
5. **Row replacement** to eliminate all other entries in column $j$.
6. Move to the next pivot row.

These operations ensure the resulting matrix is in **reduced row-echelon form** (RREF), where each pivot is 1 and is the only nonzero entry in its column.

---
</details>

### Applications

-   **Solving Systems of Linear Equations:** Gaussian elimination (transforming the augmented matrix to REF or RREF) is a standard method for finding solutions.
-   **Finding Matrix Rank:** The rank of a matrix is the number of non-zero rows (or pivots) in its Row Echelon Form.
-   **Calculating Determinants:** Row operations can simplify determinant calculations (keeping track of how operations affect the determinant).
-   **Finding Matrix Inverses:** The Gauss-Jordan elimination method (transforming $[A | I]$ to $[I | A^{-1}]$) uses row operations to find the inverse.
-   **Determining Linear Independence:** Used to check if a set of vectors is linearly independent.

### Implementation Considerations

-   The process of transforming a matrix to REF is called **Gaussian Elimination**. Transforming to RREF is called **Gauss-Jordan Elimination**.
-   **Pivoting Strategy:** When implementing, choosing the pivot element in each column is important. Using the entry with the largest absolute value in the current column (partial pivoting) can improve numerical stability, especially with floating-point numbers.
-   **Computational Complexity:** The standard Gaussian elimination algorithm has a time complexity of approximately $O(n^3)$ for an $n \times n$ matrix.
-   Handle potential division by zero when scaling rows to make pivots equal to 1 (if required for RREF) or during elimination steps if a pivot candidate is zero. SwappingOkay, let's break down thiseexample step-by-step. The goal is transform the starting matrix into **Row Echelon Form (**. Think of REF as a "staircase" pattern wh1.  Any rows consisting entirely of zeroare a the bottom.
2.  For ows tht are't all zero, the irst nn-zeo nuber (**pivot** or leading entry) is always to the right of the pivot in the row above it.
3.  Often (like in this example), the pivots are made to be 1.

# Ex 11

## Determinant

The determinant is a scalar value that can be computed from the elements of a square matrix. It encodes certain properties of the linear transformation described by the matrix and has important applications in linear algebra, geometry, and calculus.

### Compatibility Requirement

-   The determinant is only defined for **square matrices** ($n \times n$).

### Calculation Methods

*   **2x2 Matrix:**
    For a matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the determinant is:
    $$ \det(A) = |A| = ad - bc $$

*   **3x3 Matrix (Sarrus' Rule):**
    For a matrix $A = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix}$, the determinant can be calculated using Sarrus' rule:
    $$ \det(A) = a(ei - fh) - b(di - fg) + c(dh - eg) $$
    Visually: Add the products of the forward diagonals and subtract the products of the backward diagonals.
    <details>
        <summary><b>Click to view Sarrus' Rule Visualization</b></summary>
        <img src="./assets/sarrus_rule.png" alt="Sarrus Rule" width="50%" height="50%" />
        <p><i>Repeat the first two columns to the right. Add products of diagonals from top-left to bottom-right. Subtract products of diagonals from top-right to bottom-left.</i></p>
        <p>$\det(A) = (aei + bfg + cdh) - (ceg + afh + bdi)$</p>
    </details>

*   **General Method (Cofactor Expansion / Laplace Expansion):**
    The determinant can be calculated by expanding along any row or column. Expanding along the $i$-th row:
    $$ \det(A) = \sum_{j=1}^{n} (-1)^{i+j} A_{ij} M_{ij} $$
    Expanding along the $j$-th column:
    $$ \det(A) = \sum_{i=1}^{n} (-1)^{i+j} A_{ij} M_{ij} $$
    Where:
    -   $A_{ij}$ is the element in the $i$-th row and $j$-th column.
    -   $M_{ij}$ is the determinant of the $(n-1) \times (n-1)$ submatrix obtained by removing the $i$-th row and $j$-th column (called the minor).
    -   $C_{ij} = (-1)^{i+j} M_{ij}$ is the cofactor of $A_{ij}$.

### Example Calculation

*   **2x2 Example:**
    Let $A = \begin{pmatrix} 3 & 8 \\ 4 & 6 \end{pmatrix}$.
    $$ \det(A) = (3 \times 6) - (8 \times 4) = 18 - 32 = -14 $$

*   **3x3 Example (using cofactor expansion along the first row):**
    Let $B = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 4 & 5 \\ 1 & 0 & 6 \end{pmatrix}$.
    $$
    \begin{aligned}
    \det(B) &= 1 \cdot C_{11} + 2 \cdot C_{12} + 3 \cdot C_{13} \\
    &= 1 \cdot (-1)^{1+1} \begin{vmatrix} 4 & 5 \\ 0 & 6 \end{vmatrix} + 2 \cdot (-1)^{1+2} \begin{vmatrix} 0 & 5 \\ 1 & 6 \end{vmatrix} + 3 \cdot (-1)^{1+3} \begin{vmatrix} 0 & 4 \\ 1 & 0 \end{vmatrix} \\
    &= 1 \cdot (1) \cdot (4 \times 6 - 5 \times 0) + 2 \cdot (-1) \cdot (0 \times 6 - 5 \times 1) + 3 \cdot (1) \cdot (0 \times 0 - 4 \times 1) \\
    &= 1 \cdot (24) - 2 \cdot (-5) + 3 \cdot (-4) \\
    &= 24 + 10 - 12 \\
    &= 22
    \end{aligned}
    $$

### Properties

*   **Identity Matrix:** $\det(I_n) = 1$.
*   **Row/Column Operations:**
    *   Swapping two rows/columns multiplies the determinant by -1.
    *   Multiplying a row/column by a scalar $c$ multiplies the determinant by $c$.
    *   Adding a multiple of one row/column to another does *not* change the determinant.
*   **Transpose:** $\det(A^T) = \det(A)$.
*   **Product:** $\det(AB) = \det(A) \det(B)$ for square matrices $A, B$ of the same size.
*   **Inverse:** A square matrix $A$ is invertible if and only if $\det(A) \neq 0$. If invertible, $\det(A^{-1}) = 1 / \det(A)$.
*   **Triangular Matrix:** The determinant of a triangular matrix (upper or lower) is the product of its diagonal entries.
*   **Zero Row/Column:** If a matrix has a row or column consisting entirely of zeros, its determinant is 0.
*   **Dependent Rows/Columns:** If the rows or columns of a matrix are linearly dependent, its determinant is 0.

### Geometric Interpretation

*   In 2D, the absolute value of the determinant $|\det(A)|$ represents the **area scaling factor** of the linear transformation defined by matrix $A$. It tells how much the area of a shape (like the unit square) changes when transformed by $A$.
*   In 3D, $|\det(A)|$ represents the **volume scaling factor**.
*   The sign of the determinant indicates whether the transformation preserves orientation (positive determinant) or reverses it (negative determinant). A determinant of 0 means the transformation collapses the space into a lower dimension (e.g., maps a 2D area to a line or point).

<details>
    <summary><b>Click to view Geometric Interpretation Visualization (2D)</b></summary>
    <img src="./assets/determinant_geometric.png" alt="Determinant Geometric Interpretation" width="60%" height="60%" />
    <p><i>The matrix transforms the unit square (area 1) into a parallelogram. The area of this parallelogram is equal to the absolute value of the determinant of the matrix. The sign indicates orientation change.</i></p>
</details>

### Applications

*   **Solving Systems of Linear Equations:** Cramer's rule uses determinants to find solutions (though often computationally inefficient).
*   **Finding Matrix Inverses:** The adjugate matrix formula for the inverse involves determinants.
*   **Checking Invertibility:** A non-zero determinant indicates an invertible matrix.
*   **Calculating Eigenvalues:** Determinants are used in finding the characteristic polynomial ($\det(A - \lambda I) = 0$).
*   **Geometry:** Calculating areas of parallelograms/triangles and volumes of parallelepipeds/tetrahedrons.
*   **Calculus:** Used in change of variables for multiple integrals (Jacobian determinant).

### Implementation Considerations

*   Calculating determinants using cofactor expansion has a factorial time complexity ($O(n!)$), which is highly inefficient for large matrices.
*   A more efficient method is to use Gaussian elimination to transform the matrix into row echelon form (which is triangular). The determinant is then the product of the diagonal entries, adjusted by factors of -1 for row swaps and scaling factors used. This method has a complexity of $O(n^3)$.
*   Numerical stability can be an issue with floating-point numbers, especially for matrices that are close to singular (determinant close to zero). Pivoting strategies used in Gaussian elimination help mitigate this.
*   For very large matrices, specialized numerical methods are used.