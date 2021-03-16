if __name__ == '__main__':
    with open('house.csv', 'r+') as infile:
        dt = infile.read().split('\n')
    with open('dataset_truth.csv', 'r+') as infile:
        dtruth = infile.read().split('\n')
    count = 0
    score = 0
    for i, (pred, truth) in enumerate(zip(dt[1:], dtruth[1:])):
        score += (pred == truth)
        count += 1
    print(f'acc: {score / count}')
