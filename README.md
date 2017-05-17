# csv2table
可以把csv檔轉成latex表格的形式，執行程式後會將檔案輸出在終端機的螢幕上，然後複製貼上到latex的檔案中。 
（我知道這聽起來很蠢ＸＤ）

有胡亂寫幾個指令：  
`-s, --style` 可以指定表格每一欄的格式，沒有防呆，預設都是置中。  
`-c, --caption` 表格的名字，可以打中文  
`-l, --lable` 引用的標記  
`-t, --tab` 輸出的格式要不要有縮排，預設是沒有縮排  

舉例：  
``` python csv2table.py test.csv -s "|cll|" -l "table" -c "表格" -t ```  
輸出為：  
```Latex
\begin{table}  
    \centering  
    \begin{tabular}{|cll|}  
        \hline  
         & 項目一 & 項目二\\  
        \hline  
        1 & a & 甲\\  
        \hline  
        2 & b & 乙\\  
        \hline  
    \end{tabular}  
    \label{table}  
    \caption{表格}  
\end{table}  
```
記得`--style`後面接的指令要加上引號，不然執行應該會出問題（因為'|'會被視為是pipe）

