"""rondora1 main code"""
from urllib.request import urlopen, Request

url = input("Example format: 2022121715gm-0009-0000-e165b065: ")


class RunPerEachProgramRun:
    """run per each program open"""

    def __init__(self):
        openedurl = urlopen(Request("http://tenhou.net/0/log/?" +
                                    url, headers={'User-Agent': 'Mozilla'})).read()
        with open("./test/" + url, mode="wb") as filewrite:
            filewrite.write(openedurl)


paiyama = [
    {"No": 0, "paiName": "一萬", "paiCode": "1m", "paiNo": 1},
    {"No": 1, "paiName": "一萬", "paiCode": "1m", "paiNo": 1},
    {"No": 2, "paiName": "一萬", "paiCode": "1m", "paiNo": 1},
    {"No": 3, "paiName": "一萬", "paiCode": "1m", "paiNo": 1},
    {"No": 4, "paiName": "二萬", "paiCode": "2m", "paiNo": 2},
    {"No": 5, "paiName": "二萬", "paiCode": "2m", "paiNo": 2},
    {"No": 6, "paiName": "二萬", "paiCode": "2m", "paiNo": 2},
    {"No": 7, "paiName": "二萬", "paiCode": "2m", "paiNo": 2},
    {"No": 8, "paiName": "三萬", "paiCode": "3m", "paiNo": 3},
    {"No": 9, "paiName": "三萬", "paiCode": "3m", "paiNo": 3},
    {"No": 10, "paiName": "三萬", "paiCode": "3m", "paiNo": 3},
    {"No": 11, "paiName": "三萬", "paiCode": "3m", "paiNo": 3},
    {"No": 12, "paiName": "四萬", "paiCode": "4m", "paiNo": 4},
    {"No": 13, "paiName": "四萬", "paiCode": "4m", "paiNo": 4},
    {"No": 14, "paiName": "四萬", "paiCode": "4m", "paiNo": 4},
    {"No": 15, "paiName": "四萬", "paiCode": "4m", "paiNo": 4},
    {"No": 16, "paiName": "赤五萬", "paiCode": "0m", "paiNo": 0},
    {"No": 17, "paiName": "五萬", "paiCode": "5m", "paiNo": 5},
    {"No": 18, "paiName": "五萬", "paiCode": "5m", "paiNo": 5},
    {"No": 19, "paiName": "五萬", "paiCode": "5m", "paiNo": 5},
    {"No": 20, "paiName": "六萬", "paiCode": "6m", "paiNo": 6},
    {"No": 21, "paiName": "六萬", "paiCode": "6m", "paiNo": 6},
    {"No": 22, "paiName": "六萬", "paiCode": "6m", "paiNo": 6},
    {"No": 23, "paiName": "六萬", "paiCode": "6m", "paiNo": 6},
    {"No": 24, "paiName": "七萬", "paiCode": "7m", "paiNo": 7},
    {"No": 25, "paiName": "七萬", "paiCode": "7m", "paiNo": 7},
    {"No": 26, "paiName": "七萬", "paiCode": "7m", "paiNo": 7},
    {"No": 27, "paiName": "七萬", "paiCode": "7m", "paiNo": 7},
    {"No": 28, "paiName": "八萬", "paiCode": "8m", "paiNo": 8},
    {"No": 29, "paiName": "八萬", "paiCode": "8m", "paiNo": 8},
    {"No": 30, "paiName": "八萬", "paiCode": "8m", "paiNo": 8},
    {"No": 31, "paiName": "八萬", "paiCode": "8m", "paiNo": 8},
    {"No": 32, "paiName": "九萬", "paiCode": "9m", "paiNo": 9},
    {"No": 33, "paiName": "九萬", "paiCode": "9m", "paiNo": 9},
    {"No": 34, "paiName": "九萬", "paiCode": "9m", "paiNo": 9},
    {"No": 35, "paiName": "九萬", "paiCode": "9m", "paiNo": 9},
    {"No": 36, "paiName": "一筒", "paiCode": "1p", "paiNo": 11},
    {"No": 37, "paiName": "一筒", "paiCode": "1p", "paiNo": 11},
    {"No": 38, "paiName": "一筒", "paiCode": "1p", "paiNo": 11},
    {"No": 39, "paiName": "一筒", "paiCode": "1p", "paiNo": 11},
    {"No": 40, "paiName": "二筒", "paiCode": "2p", "paiNo": 12},
    {"No": 41, "paiName": "二筒", "paiCode": "2p", "paiNo": 12},
    {"No": 42, "paiName": "二筒", "paiCode": "2p", "paiNo": 12},
    {"No": 43, "paiName": "二筒", "paiCode": "2p", "paiNo": 12},
    {"No": 44, "paiName": "三筒", "paiCode": "3p", "paiNo": 13},
    {"No": 45, "paiName": "三筒", "paiCode": "3p", "paiNo": 13},
    {"No": 46, "paiName": "三筒", "paiCode": "3p", "paiNo": 13},
    {"No": 47, "paiName": "三筒", "paiCode": "3p", "paiNo": 13},
    {"No": 48, "paiName": "四筒", "paiCode": "4p", "paiNo": 14},
    {"No": 49, "paiName": "四筒", "paiCode": "4p", "paiNo": 14},
    {"No": 50, "paiName": "四筒", "paiCode": "4p", "paiNo": 14},
    {"No": 51, "paiName": "四筒", "paiCode": "4p", "paiNo": 14},
    {"No": 52, "paiName": "赤五筒", "paiCode": "0p", "paiNo": 10},
    {"No": 53, "paiName": "五筒", "paiCode": "5p", "paiNo": 15},
    {"No": 54, "paiName": "五筒", "paiCode": "5p", "paiNo": 15},
    {"No": 55, "paiName": "五筒", "paiCode": "5p", "paiNo": 15},
    {"No": 56, "paiName": "六筒", "paiCode": "6p", "paiNo": 16},
    {"No": 57, "paiName": "六筒", "paiCode": "6p", "paiNo": 16},
    {"No": 58, "paiName": "六筒", "paiCode": "6p", "paiNo": 16},
    {"No": 59, "paiName": "六筒", "paiCode": "6p", "paiNo": 16},
    {"No": 60, "paiName": "七筒", "paiCode": "7p", "paiNo": 17},
    {"No": 61, "paiName": "七筒", "paiCode": "7p", "paiNo": 17},
    {"No": 62, "paiName": "七筒", "paiCode": "7p", "paiNo": 17},
    {"No": 63, "paiName": "七筒", "paiCode": "7p", "paiNo": 17},
    {"No": 64, "paiName": "八筒", "paiCode": "8p", "paiNo": 18},
    {"No": 65, "paiName": "八筒", "paiCode": "8p", "paiNo": 18},
    {"No": 66, "paiName": "八筒", "paiCode": "8p", "paiNo": 18},
    {"No": 67, "paiName": "八筒", "paiCode": "8p", "paiNo": 18},
    {"No": 68, "paiName": "九筒", "paiCode": "9p", "paiNo": 19},
    {"No": 69, "paiName": "九筒", "paiCode": "9p", "paiNo": 19},
    {"No": 70, "paiName": "九筒", "paiCode": "9p", "paiNo": 19},
    {"No": 71, "paiName": "九筒", "paiCode": "9p", "paiNo": 19},
    {"No": 72, "paiName": "一索", "paiCode": "1s", "paiNo": 21},
    {"No": 73, "paiName": "一索", "paiCode": "1s", "paiNo": 21},
    {"No": 74, "paiName": "一索", "paiCode": "1s", "paiNo": 21},
    {"No": 75, "paiName": "一索", "paiCode": "1s", "paiNo": 21},
    {"No": 76, "paiName": "二索", "paiCode": "2s", "paiNo": 22},
    {"No": 77, "paiName": "二索", "paiCode": "2s", "paiNo": 22},
    {"No": 78, "paiName": "二索", "paiCode": "2s", "paiNo": 22},
    {"No": 79, "paiName": "二索", "paiCode": "2s", "paiNo": 22},
    {"No": 80, "paiName": "三索", "paiCode": "3s", "paiNo": 23},
    {"No": 81, "paiName": "三索", "paiCode": "3s", "paiNo": 23},
    {"No": 82, "paiName": "三索", "paiCode": "3s", "paiNo": 23},
    {"No": 83, "paiName": "三索", "paiCode": "3s", "paiNo": 23},
    {"No": 84, "paiName": "四索", "paiCode": "4s", "paiNo": 24},
    {"No": 85, "paiName": "四索", "paiCode": "4s", "paiNo": 24},
    {"No": 86, "paiName": "四索", "paiCode": "4s", "paiNo": 24},
    {"No": 87, "paiName": "四索", "paiCode": "4s", "paiNo": 24},
    {"No": 88, "paiName": "赤五索", "paiCode": "0s", "paiNo": 20},
    {"No": 89, "paiName": "五索", "paiCode": "5s", "paiNo": 25},
    {"No": 90, "paiName": "五索", "paiCode": "5s", "paiNo": 25},
    {"No": 91, "paiName": "五索", "paiCode": "5s", "paiNo": 25},
    {"No": 92, "paiName": "六索", "paiCode": "6s", "paiNo": 26},
    {"No": 93, "paiName": "六索", "paiCode": "6s", "paiNo": 26},
    {"No": 94, "paiName": "六索", "paiCode": "6s", "paiNo": 26},
    {"No": 95, "paiName": "六索", "paiCode": "6s", "paiNo": 26},
    {"No": 96, "paiName": "七索", "paiCode": "7s", "paiNo": 27},
    {"No": 97, "paiName": "七索", "paiCode": "7s", "paiNo": 27},
    {"No": 98, "paiName": "七索", "paiCode": "7s", "paiNo": 27},
    {"No": 99, "paiName": "七索", "paiCode": "7s", "paiNo": 27},
    {"No": 100, "paiName": "八索", "paiCode": "8s", "paiNo": 28},
    {"No": 101, "paiName": "八索", "paiCode": "8s", "paiNo": 28},
    {"No": 102, "paiName": "八索", "paiCode": "8s", "paiNo": 28},
    {"No": 103, "paiName": "八索", "paiCode": "8s", "paiNo": 28},
    {"No": 104, "paiName": "九索", "paiCode": "9s", "paiNo": 29},
    {"No": 105, "paiName": "九索", "paiCode": "9s", "paiNo": 29},
    {"No": 106, "paiName": "九索", "paiCode": "9s", "paiNo": 29},
    {"No": 107, "paiName": "九索", "paiCode": "9s", "paiNo": 29},
    {"No": 108, "paiName": "東", "paiCode": "1z", "paiNo": 31},
    {"No": 109, "paiName": "東", "paiCode": "1z", "paiNo": 31},
    {"No": 110, "paiName": "東", "paiCode": "1z", "paiNo": 31},
    {"No": 111, "paiName": "東", "paiCode": "1z", "paiNo": 31},
    {"No": 112, "paiName": "南", "paiCode": "2z", "paiNo": 32},
    {"No": 113, "paiName": "南", "paiCode": "2z", "paiNo": 32},
    {"No": 114, "paiName": "南", "paiCode": "2z", "paiNo": 32},
    {"No": 115, "paiName": "南", "paiCode": "2z", "paiNo": 32},
    {"No": 116, "paiName": "西", "paiCode": "3z", "paiNo": 33},
    {"No": 117, "paiName": "西", "paiCode": "3z", "paiNo": 33},
    {"No": 118, "paiName": "西", "paiCode": "3z", "paiNo": 33},
    {"No": 119, "paiName": "西", "paiCode": "3z", "paiNo": 33},
    {"No": 120, "paiName": "北", "paiCode": "4z", "paiNo": 34},
    {"No": 121, "paiName": "北", "paiCode": "4z", "paiNo": 34},
    {"No": 122, "paiName": "北", "paiCode": "4z", "paiNo": 34},
    {"No": 123, "paiName": "北", "paiCode": "4z", "paiNo": 34},
    {"No": 124, "paiName": "白", "paiCode": "5z", "paiNo": 35},
    {"No": 125, "paiName": "白", "paiCode": "5z", "paiNo": 35},
    {"No": 126, "paiName": "白", "paiCode": "5z", "paiNo": 35},
    {"No": 127, "paiName": "白", "paiCode": "5z", "paiNo": 35},
    {"No": 128, "paiName": "發", "paiCode": "6z", "paiNo": 36},
    {"No": 129, "paiName": "發", "paiCode": "6z", "paiNo": 36},
    {"No": 130, "paiName": "發", "paiCode": "6z", "paiNo": 36},
    {"No": 131, "paiName": "發", "paiCode": "6z", "paiNo": 36},
    {"No": 132, "paiName": "中", "paiCode": "7z", "paiNo": 37},
    {"No": 133, "paiName": "中", "paiCode": "7z", "paiNo": 37},
    {"No": 134, "paiName": "中", "paiCode": "7z", "paiNo": 37},
    {"No": 135, "paiName": "中", "paiCode": "7z", "paiNo": 37}
]

with open("./test/" + url, mode="r", encoding="utf-8") as readfile:
    unparsedfilecontent = readfile.read()

RunPerEachProgramRun()
