import loading_data as ld

data = ld.loading_data()
print(list(set(data['label_lst'])))
print(f'img shape: {data["img_lst"][1].shape}')
f