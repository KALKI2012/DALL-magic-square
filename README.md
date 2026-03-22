# DALL Magic Square Generator

Python implementation of the **DALL algorithm** for generating odd-order **perfect magic squares** (including the classic Lo Shu).  
Based on the paper:  
Yang, Z. (2025). *DALL: Generative Rules and Relational Structures of Odd-Order Pan-Diagonal Magic Squares*. Zenodo.  
DOI: [10.5281/zenodo.15301287](https://doi.org/10.5281/zenodo.15301287)

## Features
- Generates any odd-order perfect magic square (3, 5, 7, …)
- Includes a Python script and an interactive web page
- Verifies that all rows, columns, and both diagonal families sum to the magic constant
- Demonstrates the recursive vector logic (V1–V4) behind the DALL system

## Quick Start

### Python Version
```bash
# Clone the repository
git clone https://github.com/[KALKI2012]/dall-magic-square.git
cd dall-magic-square

# Run the script (tests D=3,5,7)
python dall_magic_square.py
```

### Web Version
Open `dall_magic_square_web.html` in any modern browser.  
Use the slider to choose an odd order (3–15) and click "Generate".

## Example Output (D=3)

```
4  9  2
3  5  7
8  1  6
```
All rows, columns, and both diagonal families sum to 15.

## Algorithm Overview

The DALL algorithm uses a recursive modular function:

$$
f(N) = 
\begin{cases}
(N + 1) \mod D^2, & N \not\equiv 0 \pmod{D} \\
(N + \Phi(k)) \mod D^2, & N \equiv 0 \pmod{D}
\end{cases}
$$
$$
\Phi(k) = mD + k, \quad m \in \{1, 2, \dots, k\}
$$

where `k` is the vector level (V1→k=1, V2→k=2, V3→k=3) and `φ(k) = mD + k` with `m ∈ {1, 2, ..., k}`. This gives:
- **V1 (k=1)**: `φ(1) = D+1`
- **V2 (k=2)**: `φ(2) = D+2, 2D+2`
- **V3 (k=3)**: `φ(3) = D+3, 2D+3, 3D+3`
- **V4 (base vector)**: step = 1

The generated squares are **perfect magic squares**: all rows, columns, and both diagonal directions (main and anti-diagonals) have the same sum.

## References

- Zenodo paper: `https://doi.org/10.5281/zenodo.15301287` 
- Author: Zongci Yang (杨宗慈) – saveearth@aliyun.com]

## License

This project is open‑source under the **MIT License**.  
Feel free to use, modify, and distribute with attribution.
