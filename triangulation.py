import cv2

traingles=[[1,37,18],[18,37,19],[19,37,38],
[19,38,20],[20,38,39],[20,39,21],
[21,39,40],[21,40,22],[22,40,28],
[28,40,29],[29,40,30],[30,40,41],
[30,31,41],[31,41,32],[1,37,2],
[2,37,42],[2,3,42],[32,31,33],
[33,31,34],[31,34,35],[31,35,36],
[3,41,42],[3,41,32],[3,50,32],
[3,49,50],[3,4,49],[4,5,49],
[5,6,49],[6,49,60],[6,7,60],
[7,60,59],[7,8,59],[8,59,9],
[9,59,58],[15,47,48],[15,48,36],
[15,54,36],[15,54,55],[15,55,14],
[14,55,13],[13,55,12],[12,55,56],
[12,56,11],[11,56,57],[11,57,10],
[10,57,9],[9,58,57],[32,50,51],
[32,51,33],[33,51,52],[33,52,34],
[34,52,53],[34,53,35],[35,53,36],
[36,53,54],[17,46,27],[27,46,26],
[26,46,45],[26,45,25],[25,44,45],
[25,44,24],[24,44,23],[23,44,43],
[23,43,28],[28,29,43],[29,43,30],
[30,43,48],[30,48,31],[31,48,36],
[17,46,16],[16,46,47],[16,15,47],
[49,50,61],[50,61,62],[50,51,62],
[51,62,63],[51,52,63],[52,63,64],
[52,64,53],[53,64,54],[54,64,65],
[54,65,55],[49,61,60],[61,60,68],
[60,68,59],[59,68,67],[59,58,67],
[58,57,67],[57,67,66],[57,66,56],
[66,56,65],[65,56,55],[37,38,42],
[38,39,42],[39,42,41],[40,41,39],
[43,44,48],[44,48,47],[44,47,45],
[46,45,47]]


triangles_edge=[[101,18,1],[101,18,19],[101,19,20],
[101,20,22],[108,1,101],[108,1,2],
[108,2,3],[108,3,4],[108,4,107],
[107,4,5],[107,5,6],[107,6,7],
[107,7,8],[107,8,106],[106,8,9],
[106,9,10],[106,10,105],[105,10,11],
[105,11,12],[105,12,13],[105,13,14],
[105,14,104],[104,15,14],[104,15,16],
[104,16,17],[104,17,103],[103,17,27],
[103,27,26],[103,26,25],[103,25,102],
[102,15,24],[102,24,23],[102,23,28],
[102,20,21],[102,21,22],[102,22,28]]

img1 = cv2.imread('Pictures/img5.jpg')
img2 = cv2.imread('Pictures/img6.jpg')

