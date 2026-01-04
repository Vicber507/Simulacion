import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Parámetros
wavelengths = np.array([650e-9, 532e-9, 450e-9])  # R, G, B (m)
dx = 10e-6
z = 0.01  # distancia final (1 cm)

# Cargar imagen
img = Image.open("imagen.png").convert("RGB")
A = np.array(img, dtype=float) / 255.0

Ny, Nx, _ = A.shape
fx = np.fft.fftfreq(Nx, dx)
fy = np.fft.fftfreq(Ny, dx)
FX, FY = np.meshgrid(fx, fy)

# Propagación
U1 = np.zeros_like(A, dtype=complex)

for i, lam in enumerate(wavelengths):
    U0 = A[:,:,i] * np.exp(0j)
    H = np.exp(-1j * np.pi * lam * z * (FX**2 + FY**2))
    U1[:,:,i] = np.fft.ifft2(np.fft.fft2(U0) * H)

I1 = np.abs(U1)**2
for i in range(3):
    if I1[:,:,i].max() > 0:
        I1[:,:,i] /= I1[:,:,i].max()

# Mostrar resultado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.imshow(A)
ax1.set_title("Apertura (RGB)", fontsize=14)
ax1.axis('off')

ax2.imshow(I1)
ax2.set_title(f"Difracción - z = {z*1e3:.2f} mm", fontsize=14)
ax2.axis('off')

plt.tight_layout()
plt.show()