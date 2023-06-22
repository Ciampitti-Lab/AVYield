from data.pre_processing import datasets


def select_data(selected_crop):
    print("Selected crop: ", selected_crop)
    select_dataset = datasets[selected_crop]
    print(select_dataset.head())
