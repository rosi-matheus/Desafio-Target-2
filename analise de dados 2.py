<row>
 <dia>1</dia>
  <valor>31490.7866</valor>
</row>
<row>
  <dia>2</dia>
  <valor>37277.9400</valor>
</row>
<row>
  <dia>3</dia>
  <valor>37708.4303</valor>
</row>
<row>
  <dia>4</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>5</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>6</dia>
  <valor>17934.2269</valor>
</row>
<row>
  <dia>7</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>8</dia>
  <valor>6965.1262</valor>
</row>
<row>
  <dia>9</dia>
  <valor>24390.9374</valor>
</row>
<row>
  <dia>10</dia>
  <valor>14279.6481</valor>
</row>
<row>
  <dia>11</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>12</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>13</dia>
  <valor>39807.6622</valor>
</row>
<row>
  <dia>14</dia>
  <valor>27261.6304</valor>
</row>
<row>
  <dia>15</dia>
  <valor>39775.6434</valor>
</row>
<row>
  <dia>16</dia>
  <valor>29797.6232</valor>
</row>
<row>
  <dia>17</dia>
  <valor>17216.5017</valor>
</row>
<row>
  <dia>18</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>19</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>20</dia>
  <valor>12974.2000</valor>
</row>
<row>
  <dia>21</dia>
  <valor>28490.9861</valor>
</row>
<row>
  <dia>22</dia>
  <valor>8748.0937</valor>
</row>
<row>
  <dia>23</dia>
  <valor>8889.0023</valor>
</row>
<row>
  <dia>24</dia>
  <valor>17767.5583</valor>
</row>
<row>
  <dia>25</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>26</dia>
  <valor>0.0000</valor>
</row>
<row>
  <dia>27</dia>
  <valor>3071.3283</valor>
</row>
<row>
  <dia>28</dia>
  <valor>48275.2994</valor>
</row>
<row>
  <dia>29</dia>
  <valor>10299.6761</valor>
</row>
<row>
  <dia>30</dia>
  <valor>39874.1073</valor>
</row>
valores = [
    31490.7866, 37277.9400, 37708.4303, 0.0000, 0.0000, 17934.2269, 0.0000, 
    6965.1262, 24390.9374, 14279.6481, 0.0000, 0.0000, 39807.6622, 27261.6304, 
    39775.6434, 29797.6232, 17216.5017, 0.0000, 0.0000, 12974.2000, 28490.9861, 

    8748.0937, 8889.0023, 17767.5583, 0.0000, 0.0000, 3071.3283, 48275.2994, 
    10299.6761, 39874.1073
]

soma_total = sum(valores)
soma_total
valores = [
    31490.7866, 37277.9400, 37708.4303, 0.0000, 0.0000, 17934.2269, 0.0000, 
    6965.1262, 24390.9374, 14279.6481, 0.0000, 0.0000, 39807.6622, 27261.6304, 
    39775.6434, 29797.6232, 17216.5017, 0.0000, 0.0000, 12974.2000, 28490.9861, 
    8748.0937, 8889.0023, 17767.5583, 0.0000, 0.0000, 3071.3283, 48275.2994, 
    10299.6761, 39874.1073
]

# Calculando a média dos valores
media_valores = sum(valores) / len(valores)

# Identificando os dias com valores não zero
dias_com_valores_nao_zero = [i + 1 for i, valor in enumerate(valores) if valor != 0.0]

print(f"Média dos valores: {media_valores}")
print(f"Dias com valores não zero: {dias_com_valores_nao_zero}")
