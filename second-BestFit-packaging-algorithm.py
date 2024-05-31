import matplotlib.pyplot as plt
import random

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Bin:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.remaining_width = width
        self.remaining_height = height
        self.rectangles = []

    def can_fit(self, rect):
        return self.remaining_width >= rect.width and self.remaining_height >= rect.height

    def place(self, rect):
        if self.can_fit(rect):
            self.rectangles.append(rect)
            self.remaining_width -= rect.width
            return True
        return False

def best_fit(rectangles, bin_width, bin_height):
    bins = [Bin(bin_width, bin_height)]
    
    for rect in rectangles:
        # Поиск лучшего контейнера, в который поместится прямоугольник
        best_bin = None
        min_remaining_space = None
        
        for bin in bins:
            if bin.can_fit(rect):
                remaining_space = bin.remaining_width * bin.remaining_height - rect.width * rect.height
                if best_bin is None or remaining_space < min_remaining_space:
                    best_bin = bin
                    min_remaining_space = remaining_space
        
        # Если подходящего контейнера не найдено, создаем новый
        if best_bin is None:
            new_bin = Bin(bin_width, bin_height)
            new_bin.place(rect)
            bins.append(new_bin)
        else:
            best_bin.place(rect)
    
    return bins

def generate_random_rectangles(num_rectangles, max_width, max_height):
    return [Rectangle(random.randint(1, max_width), random.randint(1, max_height)) for _ in range(num_rectangles)]

def visualize_bins(bins):
    fig, ax = plt.subplots(figsize=(12, 8))
    for i, bin in enumerate(bins):
        x_offset = i * (bin.width + 10)  # 10 units space between bins
        y_offset = 0
        for rect in bin.rectangles:
            rect_patch = plt.Rectangle((x_offset, y_offset), rect.width, rect.height, edgecolor='black', facecolor='lightblue')
            ax.add_patch(rect_patch)
            y_offset += rect.height
    plt.xlim(0, len(bins) * (bins[0].width + 10))
    plt.ylim(0, max(bin.height for bin in bins))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

num_rectangles = 20
max_rect_width = 50
max_rect_height = 50
bin_width = 100
bin_height = 100

rectangles = generate_random_rectangles(num_rectangles, max_rect_width, max_rect_height)

bins = best_fit(rectangles, bin_width, bin_height)

visualize_bins(bins)
