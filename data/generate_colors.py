import numpy as np

def generate_sample():
    """
    Generate a color patch under illumination.
    Label depends on absolute hue, NOT invariant color.
    """
    # base hue in [0, 1]
    hue = np.random.uniform(0.2, 0.8)

    # illumination shift
    illumination = np.random.uniform(-0.15, 0.15)

    perceived_color = hue + illumination

    # clamp
    perceived_color = np.clip(perceived_color, 0, 1)

    # label depends on ABSOLUTE hue
    label = int(hue > 0.5)

    return perceived_color, illumination, label


def generate_dataset(n=5000):
    X, illum, y = [], [], []
    for _ in range(n):
        c, i, l = generate_sample()
        X.append(c)
        illum.append(i)
        y.append(l)

    return np.array(X), np.array(illum), np.array(y)


if __name__ == "__main__":
    X, I, y = generate_dataset(1000)
    print(X.shape, y.mean())
