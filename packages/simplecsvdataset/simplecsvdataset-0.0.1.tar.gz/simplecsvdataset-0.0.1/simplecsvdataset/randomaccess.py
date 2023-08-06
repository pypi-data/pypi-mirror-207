import os
import glob
import pandas as pd
from torch.utils.data import Dataset


class RandomAccessCsvsDataset(Dataset):
    def __init__(self, folder_path, file_pattern, x_columns, y_columns, transform=None):
        self.folder_path = folder_path
        self.file_pattern = file_pattern
        self.x_columns = x_columns
        self.y_columns = y_columns
        self.transform = transform
        self.file_list = glob.glob(os.path.join(folder_path, file_pattern))
        self.line_counts = self.get_line_counts()

    def get_line_counts(self):
        line_counts = []
        total_lines = 0
        for file in self.file_list:
            with open(file, 'r') as f:
                lines = sum(1 for line in f) - 1  # Subtract 1 for header
            line_counts.append(lines)
            total_lines += lines
        return line_counts

    def __len__(self):
        return sum(self.line_counts)

    def __getitem__(self, idx):
        # Find the file containing the idx-th data
        file_idx = 0
        while idx >= self.line_counts[file_idx]:
            idx -= self.line_counts[file_idx]
            file_idx += 1

        # Read the corresponding line from the file
        file_path = self.file_list[file_idx]
        df = pd.read_csv(file_path, skiprows=idx + 1, nrows=1, header=None)

        # Extract x and y variables
        x_data = df.loc[:, self.x_columns].values
        y_data = df.loc[:, self.y_columns].values

        # Apply the transform if provided
        if self.transform:
            x_data, y_data = self.transform(x_data, y_data)

        return x_data, y_data


