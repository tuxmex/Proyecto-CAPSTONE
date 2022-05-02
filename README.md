# Proyecto CapStone UTNG
[![Contribuidores][contribuidores-shield]][contributors-url]

## contenido
<details>
  <summary>Tabla contenidos</summary>
  <ol>
    <li>
      <a href="#acerca-del-proyecto">Acerca Del Proyecto</a>
      <ul>
        <li><a href="#construido-con">Construido Con</a></li>
      </ul>
    </li>
    <li>
      <a href="#iniciando">Iniciando</a>
      <ul>
        <li><a href="#requisitos">Prerrequisitos</a></li>
        <li><a href="#instalacion">Instalación</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#guias">Guias</a></li>
    <li><a href="#contribucion">Contribución</a></li>
    <li><a href="#licencia">licencia</a></li>
    <li><a href="#contacto">Contacto</a></li>
    <li><a href="#participantes">Participantes</a></li>
  </ol>
</details>

<!-- Acerca del proyecto -->
## Acerca del proyecto

### Nombre del proyecto
**Smart Green Wall**

**SGW-Pared Verde Inteligente para Casa-Habitación:**
### Justificación del proyecto

> Existen numerosos factores biológicos, psicológicos y sociales con impacto prominente en la salud mental de las personas adultas mayores, como la demencia y depresión, siendo éstas las que más se presentan este grupo de personas. Aparte, de componentes derivados de los procesos normales de envejecimiento o de enfermedades médicas diversas, eventos como la muerte de un ser querido, la jubilación o la discapacidad.

> El presente proyecto se enfoca principalmente en adultos mayores de la tercera edad, este grupo de presonas presenta discapacidades físicas que le impiden realizar actividades cotidianas que normalmente realizaba, la actividad de regado de plantas en el hogar ofrece grandes beneficios, según varios estudios revelan que:

-	Media hora diaria dedicada a cuidar plantas reduce significativamente los niveles de estrés.
- El cuidado de las plantas nos ayuda a desconectar, aumentan nuestra autoestima y capacidad de organización.
-	Nos ayudan a socializar.
- Seguir adquiriendo responsabilidades.
- Aumentan la sensación de amor en el hogar.
- Organizar nuestra mente

> Para la ejecución y puesta en el marcha del proyecto, se implementará un sistema de Internet de las Cosas y un Sistema Móvil, que permita controlar y semi-automatizar el riego de plantas a través de sensores que medirán la temperatura, humedad, PH, luminosidad. Actuadores, que permitirán realizar el riego semi-automatizado e indicar mediante una aplicación web, el estado o condiciones de las variables antes mencionadas; por último, una aplicación móvil que monitorea y controla el riego.

### Objetivo del proyecto: 

> Apoyar a adultos mayores con limitaciónes físicas por la edad mediante un sistema de IoT para riego semiautomatizado de plantas en el hogar.

### Descripción general del proyecto

> Este proyecto consiste generar un prototipo que propone optimizar el riego y cuidado de plantas a través del análisis de datos tomados por los sensores, validando decisiones que actúen en los lugares donde los usuarios tienen difícil acceso automatizando tareas para personas adultas mayores.


### Material de uso:

<table> <tr> <th>Componente</th><th>Imagen</th><th>Descripción</th><th>Cantidad</th></tr>
  <tr>
    <td>Raspberry Pi 4</td>
    <td>
    <img src="https://user-images.githubusercontent.com/36056832/165995675-da53df0d-9c67-46af-94e3-22f30ad2aa4d.png" alt="Raspberry Pi 4" width="100"/>
    </td>
     <td><ul><li>Raspberry Pi 4 Modelo B 8GB RAM Original Uk.<li>Memoria microSD 32GB Clase 10 A1 con adaptador.<li>Cable microHDMI a HDMI 1.5m.<li>Carcasa con soporte para ventilador.<li>Ventilador 5VDC con tornillos y tuercas.<li>Fuente 5V 3A USB-C con Switch On/Off.<li>Kit de disipadores de calor cobre y aluminio con cinta térmica adherible.</ul></td>
    <td>1</td>
  </tr> 
  <tr>
    <td>ESP32 Cam</td>
    <td>
    <img src="https://user-images.githubusercontent.com/36056832/165996397-e9527b13-6ad4-4e73-a732-7721e0ffac59.png"  alt="ESP32 Cam" width="100"/>
    </td>
    <td><ul><li>Voltaje: 5 V<li>CPU de 32 bits de doble núcleo de baja potencia para procesadores de aplicaciones<li>Frecuencia principal de hasta 240 MHz<li>Potencia de cálculo de hasta 600 DMIPS<li>SRAM integrado de 520 KB<li>PSRAM externo de 4 M<li>Es ideal para interfaces como: UART. SPI. I2C. PWM. ADC. DAC<li>Soporta cámaras OV2640 y OV7670 (flash incorporado)<li>Apoyo imagen WiFi subir<li>Apoyo TF tarjeta</ul></td>
    <td>1</td>
  </tr> 
  <tr>
    <td>Sensor DHT11</td>
    <td>
    <img src="https://user-images.githubusercontent.com/36056832/165996618-0b719509-9c81-405a-bef5-aabef6623a2b.png" alt="DHT11" width="100"/>
    </td>
    <td> <ul><li>Alimentación: 3.3 ~ 5 V<li>Rango de medición de temperatura: 0 ~ 50 °C<li>Precisión de medición de temperatura: ± 2.0 °C<li>Resolución Temperatura: 0.1 °C<li>Rango de medición de humedad: 20 % ~ 90 % RH<li>Precisión de medición de humedad: 4 % RH<li>Resolución Humedad: 1 % RH<li>Salida digital<li>Orificio de perno fijo para una fácil instalación</ul></td>
    <td>1</td>
  </tr> 
    <tr>
    <td>Sensor de Humedad Tierra LY69</td>
    <td>
       <img src="https://user-images.githubusercontent.com/36056832/165997309-ef9301b5-2694-467e-8d97-5c2c05bd4918.png" alt="yl-69" width="100"/>
    </td>
    <td><ul><li>Voltaje de entrada: 3.3 – 5 VCD<li>A0: Salida analógica que entrega una tensión proporcional a la humedad.<li>D0: Salida digital, este módulo permite ajustar cuando estará en alto y cuando en bajo según la humedad<li>Consiste en una sonda YL - 69 con dos terminales separados adecuadamente y un módulo YL - 38 que contiene un circuito comparador LM393 SMD (de soldado superficial) muy estable, un led de encendido y otro de activación de salida digital. Este último presenta 2 pines de conexión hacia el módulo YL - 69, 2 pines para la alimentación y 2 pines de datos. VCC, GND, D0, A0</ul></td>
    <td>1</td>
  </tr> 
  <tr>
    <td>Sensor de PH014</td>
    <td>
     <img src="https://user-images.githubusercontent.com/36056832/166008733-66e4407a-3c8f-4bff-bff9-a997bb99a8de.png" alt="Sensor de PH" width="100"/>
    </td>
    <td><ul><li>Modulo: PH-4502C <li>Voltaje de Alimentación: 5V <li>Corriente: 10mA <li>Dimensiones: 42 X 32 X 20 mm Electrodo E201-BNC <li>Tipo de sonda: Grado de laboratorio. <li>Tiempo de Respuesta: 5 seg <li>Rango de detección: 0 ~ 14.(acido /base) <li>Rango de temperatura:0 – 80°C <li>Temperatura de trabajo:10~50°C <li>Humedad de trabajo: 95 RH sin condensación</ul> </td>
    <td>1</td>
  </tr> 
  <tr>
    <td>Fotoresistencia</td>
    <td><img src="https://user-images.githubusercontent.com/36056832/166063254-aa64a4c1-65ac-457a-8662-409cbf5e6833.png" width="100" /></td>
    <td><ul><li>Función: Detector de luz<li>Chip principal: LM393<li>Voltaje de alimentación mínimo: 3.3 V<li>Voltaje de alimentación máximo: 5 V<li>Tipo de salida: Digital<li>Distribución de pines:<ul><li>Pin de alimentación VCC: 3.3 V - 5 V<li>Pin de alimentación 0 V: GND<li>Pin de OUT: Salida digital<li>Indicador de alimentación: LED rojo<li>Indicador de salida digital: LED verde<li><li>Dimensiones: 41 mm X 14 mm<li>Número de pines: 3
      Voltaje: 3.3v ~ 5v<li>Comparador LM393<li>Sensibilidad Ajustable</ul></td>
    <td>1</td>
  </tr> 
  <tr>
    <td>Sensor de Lluvia</td>
    <td>
    <img src="https://user-images.githubusercontent.com/36056832/166009366-c9d2c965-0ec4-49e9-9104-ea9cdb06403b.png" alt="Sensor de lluvia" width="100" />
   </td>
    <td><ul><li>Tensión de funcionamiento: 3.3V -5 V<li>Sensibilidad ajustable por potenciómetro<li>Modo de salida dual : analógica y digital<li>LED rojo – indicador de encendido<li>LED verde – indicador de salida de conmutación digital<li>Medidas PCB: 3 x 1.5 cm<li>Medidas de sensor: 5.4 x 3.9 cm</ul></td>
    <td>1</td>
  </tr> 

  <tr>
    <td>Electro Válvula de pulso +/-4.5V para control de flujo con ahorro de energía para tuberías de 1/2 pulgada cobre</td>
    <td><img src="https://user-images.githubusercontent.com/36056832/166064811-69640693-dd5d-4715-86e5-f49ec7a59ae4.png" width="100"/></td>
    <td><ul><li>Totalmente metálico<li>Control de apertura o de cierre con un sólo pulso de &gt;30ms<li>Impedancia de entrada: 9 Ohms +/-5% (@20°C)<li>Temperatura de trabajo: 1 a 80°C<li>Voltaje de trabajo: 4.5V<li>Presión de agua: 0.02 a 1MPa<li>Para apertura, es pulso POSITIVO y para cierre es pulso NEGATIVO</ul></td>
    <td>1</td>
  </tr> 
  <tr>
    <td>Motor a pasos</td>
    <td><img src="https://user-images.githubusercontent.com/36056832/166065075-3de31310-6500-41a1-a5a0-23205cb3ebb4.png" width="100"/>
</td>
    <td><ul><li>Voltaje: 5V<li>Consumo corriente: 55mA aprox.<li>Ángulo de paso: 5.625 x 1/64.<liReducción: 1/64.<li>Puede ser controlado por un chip ULN2003.<li>También se puede conectar como 2 fases para usar.<li>Dimensiones: 31 * 27 * 19 mm<li>Peso: 35g.</ul></td>
    <td>4</td>
  </tr> 
    <tr>
    <td>Relevador</td>
    <td><img src="https://user-images.githubusercontent.com/36056832/166065203-9a1ea36b-8948-4ecb-adbe-8bfd1d670b33.png" width="100" /></td>
      <td><ul><li>Número de serie: 2ph63083a</li><li>Voltaje de operación: 5V DC</li><li>Máxima salida del relevador (Voltaje/ Corriente): DC 30V/10A, AC 250V/10A</li><li>Rangos de corriente: 10 A (NO) y 5 A (NC)</li><li>Protocolo de comunicación: TTL (3.3 V o 5 V)<li>Tiempo de acción: 10 ms/ 5 ms</li><li>
        Tamaño : 75 mm x 55 mm x 19.3 mm (largo,ancho, alto)</li><li>Peso: 61 gramos</li><li>Pines:Input: : IN1, IN2, IN3, IN4 , VCC, GND
Output: Conector hacia la carga(ejemplo, bombilla, bomba de agua,etc). La terminal de relés son COM, NO y NC (Común, Normalmente Abierto y Normalmente Cerrado  respectivamente) están en la  terminal de tornillo,Jumper JDVCC, VCC y GND</li></ul></td>
    <td>4</td>
  </tr> 
    <tr>
    <td>Motor CD</td>
    <td><img src="https://user-images.githubusercontent.com/36056832/166065332-364f3cd0-4f18-44f7-85aa-6ad243851ad4.png" width="100" /></td>
      <td><ul><li>Velocidad De 15000 a 18000 RPM</li><li>Motor 25 x 15 mm</li><li>Engrane</li><li>Peso 16g</li></td>
    <td>4</td>
  </tr> 
</table>

#### Requerimientos
<table>
  <tr>
    <th>No.</th>
      <th>Requerimiento</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Medición de variables a partir de sensores de temperatura, humedad, PH, lluvia, luminosidad.</td>
  </tr>
  
  <tr>
    <td>2</td>
    <td>Almacenamiento de datos de manera continua y permanente.</td>
  </tr>
  
  <tr>
    <td>3</td>
    <td>Graficar los datos almacenados para su análisis en línea</td>
  </tr>
  <tr>
    <td>4</td>
    <td>Activar el riego automatizado de acuerdo al analisis de datos.</td>
  </tr>
  
  <tr>
    <td>5</td>
    <td>Control a partir de aplicación móvil de riego, sombra y protección.</td>
  </tr>
  <tr>
    <td>6</td>
    <td>Notificar alertas a partir del estado de las variables que involucren un riesgo para la planta.</td>
  </tr>
</table>

#### Diagrama inicial

![image](https://user-images.githubusercontent.com/96089377/165986643-432dfef7-ffff-4755-a768-ecdb5e8252b4.png)

### Prototipo de pared verde


<!-- Construido con -->


<!-- Construido con -->
### Construido con
Construido con.

<!-- Iniciando -->
## Iniciando
Iniciando.

<!-- Requisitos -->
### Requisitos
Requisitos.

<!-- Instalación -->
### Instalacion
Instalación.

<!-- Uso -->
### Uso
Uso.

## Guias
Guias.

## contribucion
Contribucion.

## Licencia
Licencia.

## Contacto
Contacto.

## Participantes
* [Gerardo Reyna Ibarra]()
* [Anastasio Rodríguez García]()
* [Gabriel Barrón Rodríguez]()

[contribuidores-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
