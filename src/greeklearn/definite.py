hello = 'apa'

nisse = f"""
% Please add the following required packages to your document preamble:
% \usepackage{multirow}
\begin{table}[]
\begin{tabular}{llllllllll}
 & \multicolumn{3}{l}{}    & \multicolumn{3}{l}{}    & \multicolumn{3}{l}{}                                      \\
 &  &                   &  &  &                   &  &                   &                   &                   \\
 &  & \multirow{2}{*}{} &  &  & \multirow{2}{*}{} &  & \multirow{2}{*}{} & \multirow{2}{*}{} & \multirow{2}{*}{} \\
 &  &                   &  &  &                   &  &                   &                   &                   \\
 &  & \multirow{2}{*}{} &  &  & \multirow{2}{*}{} &  &                   & \multirow{2}{*}{} &                   \\
 &  &                   &  &  &                   &  &                   &                   &                  
\end{tabular}
\end{table}
"""

print(nisse)