from fractions import Fraction

mtx = []
filePath = input('File path:')  # 输入矩阵文件路径
accurateResult = input('Accurate result? (Y/N)')
determinant = 1
totalExt = 0
if accurateResult == 'Y' or accurateResult == 'y':
    acr = 1
else:
    acr = 0

# 读取文件
with open(filePath, 'r') as file:
    print('Reading file...')
    fileContent = file.readlines()
    mtxSize = int(fileContent[0])
    for lt1 in range(mtxSize):
        mtx.append(fileContent[lt1 + 1].split(' '))
print('Complete!')

# 格式化数字
print('Transforming elements...')
for lt2 in range(mtxSize):
    for lt3 in range(mtxSize):
        if acr:
            mtx[lt2][lt3] = Fraction(mtx[lt2][lt3])
        else:
            mtx[lt2][lt3] = float(Fraction(mtx[lt2][lt3]))
print('Complete!')


# 行交换
def row_exchange(col):
    nzrow = []
    zrow = 0
    zmat = []
    ext = 0
    for lt4 in range(mtxSize - col + 1):
        if mtx[col - 1 + lt4][col - 1] != 0:
            nzrow.append(col - 1 + lt4)
            for lt5 in range(lt4):
                if mtx[col - 1 + lt5][col - 1] == 0:
                    ext += 1
        else:
            zmat.append(mtx[col - 1 + lt4])
            zrow += 1
    for lt6 in range(zrow):
        mtx.remove(zmat[lt6])
    mtx.extend(zmat)
    return ext


# 行倍加
def row_replace(col):
    if mtx[col - 1][col - 1] == 0:
        return 1
    else:
        for lt7 in range(mtxSize - col):
            mtn = mtx[col + lt7][col - 1] / mtx[col - 1][col - 1]
            for lt8 in range(mtxSize - col + 1):
                mtx[col + lt7][col - 1 + lt8] -= mtx[col - 1][col - 1 + lt8] * mtn
        return 0


# 计算行列式
print('Calculating...')
for lt9 in range(mtxSize - 1):
    totalExt += row_exchange(lt9 + 1)
    pause = row_replace(lt9 + 1)
    if pause:
        determinant = 0
        break
determinant *= (-1) ** totalExt
for lt10 in range(mtxSize):
    determinant *= mtx[lt10][lt10]
print('Done.')
print(f'\nDeterminant:{determinant}')
if acr:
    print(f'Float:{float(determinant)}')
