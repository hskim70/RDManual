
TSG
===

.. figure:: media/image001.*
   :name: 20_tsg_image001

   **TSG** example

**RecurDyn**/**TSG** (Time Signal Generator) is a toolkit that generates the Input Signals which can be applied to MBD or MFBD model. In other words, if the Target Signals are obtained, which are measured as accelerations, velocities, displacements, and so on at the specific locations of a physical model through the experimental test, **RecurDyn**/**TSG** can find out the Input Signals to match the Target Signals.

TSG Overview
------------

**RecurDyn**/**TSG** (Time Signal Generator) generates Input Signals by using the signal processing. After the Target Signals are obtained such as accelerations, velocities, displacements, and so on at the specific locations of a physical model in the experimental test, **RecurDyn**/**TSG** can find out Input Signals so that the Target Signals can be matched after simulation. After that, the Input Signals can be applied to Forces or Motions (displacement, velocity,
acceleration) as function expressions in the MBD model.

In experimental test, test engineers can measure Experiment Data such as accelerations, forces, angular position and displacements at some location of the structure. However, the measured data can’t be applied directly to the MBD model in **RecurDyn** because the MBD model can’t be built considering all non-linear properties of physical model. That means that the MBD model is different with the physical model.
Therefore, it is needed to calculate the new Input Signals of the MBD model in order to match the measured signals of the physical model. If the Output Signals of MBD are similar to the measured signals after applying the new Input Signal to the MBD model, the MBD Model can guarantee the similar model compared to the physical model.

.. figure:: media/image002.png
   :name: 20_tsg_image002

   **Target Signals** and **Input Signals**

TSG Terminology

-  **Target Signals** are user-defined signals that we want to reproduce and that has been measured experimentally.

-  **Response Signals** are Output Signals of **RecurDyn** at the location of the virtual **Sensors** during iterative simulation.
   These signals at the end of the process have to match the Target Signals.

-  **Drive Signals** are Input Signals of MBD model at the location of the virtual **Actuators**.

-  **Actuator** Defines **Drive Signal Locations** applied to Motion or Force on the Joint or Force elements on a MBD Model.

-  **Sensor** Defines **Response Signal Locations** to match user-defined Target Signals as a general **Expression.**

.. figure:: media/image003.png
   :name: 20_tsg_image003

   **TSG Terminology**

TSG Procedure

#. **Set up virtual Actuators & Sensors.** This implies that the user needs to define the location, type and direction of the measurement in **RecurDyn**.

#. **Define an association** between the sensors and **Target Signals**.

#. **Calculate FRF (Frequency Response Function)** after simulation.

#. **Correct** the drive signal **iteratively using the error** between Target Signals and Response Signals.

.. figure:: media/image004.png
   :name: 20_tsg_image004

   **TSG Procedure flowchart**

Functions for TSG
-----------------

Several functions are supported to simulate **TSG**.

.. figure:: media/image005.png
   :name: 20_tsg_image005

   **Signal**, **Simulation**, and **Result** group in the **TSG** tab

Signal
~~~~~~

You should set following three entities.

.. figure:: media/image006.png
   :name: 20_tsg_image006

   **Signal** group in the **TSG** tab

Actuator
^^^^^^^^

**Actuator** should be created at least one to simulate. **Actuator** is an input of the **TSG** model. The concept of both **TSG**/**Actuator** and **Control**/**Plane Input** is the same.

.. figure:: media/image007.png
   :name: 20_tsg_image007

   **Actuator** icon of the **Signal** group in the **TSG** tab

.. figure:: media/image008.png
   :name: 20_tsg_image008

   **Actuator List** dialog box

-  **Use**: Determines whether or not to use.

-  **Name**: Defines a name.

-  **Add**: Adds a row to the end of the table.

-  **Insert**: Inserts a row where the cursor is and move the current and later rows down.

-  **Delete**: Deletes the row where the cursor is and move the later rows up.

Step to create an Actuator

.. figure:: media/image009.png
   :name: 20_tsg_image009

   Usage of an Actuator

#. Click **Add** in the **Actuator** **List** dialog box.

#.  Rename an actuator.

#.  Select a force or a joint entity to set the actuator.

#.  Click **EL**.

#.  Click **Create** in **Expression List** dialog box.

#.  Rename an **Expression** name.

#. Edit the actuator using “\ **TACT(Acutator_ID)**\ ” expressions in each actuator element.

Sensor
^^^^^^

**Sensor** should be created at least one to simulate. **Sensor** is an output of the **TSG** model. The concept of both **TSG**/**Sensor** and **Control**/**Plane Output** is the same.

.. figure:: media/image010.png
   :name: 20_tsg_image010

   **Sensor** icon of the **Signal** group in the **TSG** tab

.. figure:: media/image011.png
   :name: 20_tsg_image011

   **Sensor List** dialog box

-  **Use**: Determines whether or not to use.

-  **Name**: Defines a name.

-  **Expression**: Defines an expression function.

-  **Add**: Adds a row to the end of the table.

-  **Insert**: Inserts a row where the cursor is and move the current and later rows down.

-  **Delete**: Deletes the row where the cursor is and move the later rows up.

Step to create a Sensor

.. figure:: media/image012.png
   :name: 20_tsg_image012

   Usage of a sensor

#. Click **Add** in **Sensor List** dialog box.

#. Rename an **Expression** name.

#. Edit an **Expression**.

Target
^^^^^^

**Target** should be set to simulate.

.. figure:: media/image013.png
   :name: 20_tsg_image013

   **Target** icon of the **Signal** group in the **TSG** tab

There are two tabs in **Target Output List** dialog.

-  **Target Output List** tab: Set **Target** Signal by choosing a
   “\*.TARGET” file.

-  **Target Output Function** tab: Making “\*.TARGET” file from a signal file “\*.CSV”.

Step to set Target

.. figure:: media/image014.png
   :name: 20_tsg_image014

   Example to set a target

#. Move to **Target Output Function** tab in Target Output List dialog.

#. Select a “\*.CSV” file which has the target sensor signal(s).

#. Set target output “\*.TARGET” file name and path.

#. Click **Create Target Output File**.

#. Move to **Target Output List** tab in **Target Output List** dialog box.

#. Check loading the “\*.TARGET” file or select another “\*.TARGET”
   file.

Target Output List tab
''''''''''''''''''''''

.. image:: media/image015.png

The list cannot be modified. The list is always the same with created **Sensor** list. Because, the **Target** channels should be the same with the created **Sensor** channels.

<Check>Figure 1 **Target Output List** dialog box [**Target Output List** tab]

-  **Target Output File (\*.TARGET)** : \*.TARGET file can be set by clicking **…**.

-  **Plot**: If a \*.TARGET file is set and some plot check box in the list are checked, then the user can see the **Target signal** of choosing Sensor channel by clicking **Plot**.

   .. figure:: media/image016.png
      :name: 20_tsg_image016

      **Plot** example of **Target Output List** tab

Target Output Function tab
''''''''''''''''''''''''''

The list cannot be modified. The list is always the same with created **Sensor** list. Because, the **Target** channels should be the same with the created **Sensor** channels.

.. figure:: media/image017.png
   :name: 20_tsg_image017

   **Target Output List** dialog box [**Target Output Function** tab]

-  **Target Signal (\*.CSV)**: “\*.CSV” file should be needed. All data of “\*.CSV” should be CSV (Comma-Separated Values). And there’s no needed header strings on first line. The number of columns should be 2 times of the number of sensors. Because every odd column should be a time data.

   .. figure:: media/image018.png
      :name: 20_tsg_image018

      CSV file format for **Target Signal**

-  **Plot**: User can choose plot view or not.

-  **Windowing**: If this checkbox is checked, then the generated target signal will be considered the windowing function. Default is unchecked.

-  **Time offset**: If this value is set, then the time data of the CSV Signal will be considered as (Time_CSV-Time_Offset). Default value is 0.

-  **Plot**: If a “\*.CSV” is set and some plot check box are checked, then user can see the signal data on the opened scope dialog.

-  **Sampling Frequency (Hz)**: Sampling Frequency (Hz) should be set.

-  **End Time** (s): End Time (s) should be set. The number of target signal data should be (**Sampling_Frequency \* End_Time + 1**).

-  **Windowing Parameter for Target Signals**: If the check box is selected, then a windowing function will be considered. Linear trapezoidal function is always computed.

-  **Data Size**: A natural value greater than 0 should be set. And the Data Size should be lower than the number of signal data.

-  **Linear/Step5**: Two interpolation function types are available for windowing function. Default is **Step5** function.

-  **Time Length** (s): A real number greater than 0.0 should be set.

   .. figure:: media/image019.png
      :name: 20_tsg_image019

      **Windowing function** for generating “\*.TARGET” file

.. figure:: media/image020.png
   :name: 20_tsg_image020

   Comparison of the interpolation types for **Windowing function**

-  **Target Output File (\*.TARGET)**: Defines a file name and path by clicking **…**.

-  **Create Target Output File**: Generates the \*.TARGET file by clicking this button.

Simulation
~~~~~~~~~~

.. figure:: media/image021.png
   :name: 20_tsg_image021

   **Simulation** group in the **TSG** tab

FRF
^^^

FRF (Frequency Response Function) is should be needed to simulation in **TSG** toolkit.

.. figure:: media/image022.png
   :name: 20_tsg_image022

   A schematic diagram of the **TSG** model

FRF can be computed like as <Check>equation (1) on the frequency domain.

.. math:: \begin{aligned}   & \mathbf{F}(s)\mathbf{A}(s)=\mathbf{S}(s) \\    & \mathbf{F}(s)=\mathbf{S}(s){{\mathbf{A}}^{-1}}(s) \\    \end{aligned}
   :label: 20_tsg_eq001


Where, :math:`\mathbf{A}(s)` and :math:`\mathbf{S}(s)` are Actuator Signal and Sensor Signal on the frequency domain. The :math:`s` means a frequency coordinate. The :math:`\mathbf{F}(s)`
is defined as FRF (Frequency Response Function) in the **TSG**.

The signals both :math:`\mathbf{A}(s)` and :math:`\mathbf{S}(s)` are computed using FFT (Fast Furieror Transfom).

.. math:: \begin{aligned}   & \mathbf{A}(t)\xrightarrow{FFT}\mathbf{A}(s) \\    & \mathbf{S}(t)\xrightarrow{FFT}\mathbf{S}(s) \\    \end{aligned}
   :label: 20_tsg_eq006


After computing FRF, inverse FRF (:math:`{{\mathbf{F}}^{-1}}(s)`) will be computed. Generally, the inverse FRF can be computed by the Pseudo-inverse method.

.. figure:: media/image023.png
   :name: 20_tsg_image023

   **FRF** icon of the **Simulation** group in the **TSG** tab

There are two tabs in **FRF** dialog box.

-  **FRF** tab: There are analysis options to generate **FRF**.

-  **FRF Result** tab: User can check the **FRF**, the **inverse FRF**,
   the actuator signals and the sensor signals.

.. figure:: media/image024.png
   :name: 20_tsg_image024

   **FRF** dialog box

Step for computing FRF

.. figure:: media/image025.png
   :name: 20_tsg_image025

   Usage **FRF** simulation

#. Click **FRF** icon.

#. Set **Start** and **End Frequencies**.

#. Click **Analysis Setting**.

#. Set the **End Time** on the **Dynamic/Kinematic Analysis** dialog.
   The `End Time <#EndTime_Target>`__ should be the same of the generated “\*.TARGET” file.

#. Set **Step** on the **Dynamic/Kinematic Analysis** dialog. The **Step** should be the same with (Sampling_Frequency \* End_Time).

#. Click **OK** to leave the **Dynamic/Kinematic Analysis** dialog.

#. Set FRF file name and path on the **FRF** dialog.

#. Click **Simulation** for computing **FRF** and generating “\*.FRF”
   file.

FRF tab
'''''''

All signal entities (Actuator, Sensor and, Target) should be already set to simulate FRF.

.. figure:: media/image026.png
   :name: 20_tsg_image026

   **FRF** dialog box [**FRF** tab]

-  **Sampling Frequency (Hz)**: User cannot change this value. This value is the Sampling Frequency (Hz) of loaded “\*.TARGET” data.

-  **Actuator Signal Generation for Computing FRF**: The Actuator signals (called drive signals) for computing FRF is using a Chirp signal (A sweep function) using following two parameters.

-  **Start Frequency (Hz)**: Default value is 0.01 Hz.

-  **End Frequency (Hz)**: Default value is 100.0 Hz.

   .. figure:: media/image027.png
      :name: 20_tsg_image027

      **Chirp** signals

-  **Advanced Option**: Currently user can change to magnitude data of each Actuator channels. Default magnitude is set to 1.0.

   .. figure:: media/image028.png
      :name: 20_tsg_image028

      **Advanced Option** dialog box

-  **FRF File (\*.FRF)**: Defines a file name and path by clicking **…**.

-  **Analysis Setting**: **Dynamic/Kinematic Analysis** dialog is opened. Because, currently **TSG** is only supported dynamic/kinematic analysis. The **End Time** and **Step** should be match on **TSG** setting.

-  **End Time** data on the **Dynamic/Kinematic Anlaysis** dialog should be the same with the `End Time <#EndTime_Target>`__ of “\*.TARGET”
   data.

-  **Step** data on the **Dynamic/Kinematic Anlaysis** dialog should be set with (End_Time \* Sampling_Frequency).

   .. figure:: media/image029.png
      :name: 20_tsg_image029

      **Dynamic/Kinematic Analysis** dialog

-  **Simulate**: Computes **FRF** and generate “\*.FRF” file.

FRF Result tab
''''''''''''''

Using this dialog, user can check the **FRF**, **inverse FRF**,
**Actuator signals and, Sensor Signals**. In order to check, the
“\*.FRF” file is needed.

.. figure:: media/image030.png
   :name: 20_tsg_image030

   **FRF** dialog box [**FRF Result** tab]

.. figure:: media/image031.png
   :name: 20_tsg_image031

   **FRF File** setting

-  **FRF File (\*.FRF)**: Defines “\*.FRF” file by clicking **…**.

-  **FPLT**: Checks the **FRF** and the **inverse FRF** functions with Plot windows.

   .. figure:: media/image032.png
      :name: 20_tsg_image032

      Plot view for **FRF** and **Inverse FRF** by clicking **FPLT**

   .. figure:: media/image030.png
      :name: 20_tsg_image030_1

      **Drive Signal** region on the **FRF Result** tab

-  **Iteration Number**: Defines the **Iteration Number**. **Iteration Number** means the simulation count value for computing **FRF**. And the **Iteration Number** is always the same with the number of **Actuator** channels.

-  **Drive Signal**

-  **Plot** check box in list view

-  **Export**: Generate “\*.TAI” file including the **Actuator** signals on time domain.

-  **Plot**: User can see the signal data on the opened scope dialog.

   .. figure:: media/image030.png
      :name: 20_tsg_image030_2

      **Response Signal** region on the **FRF Result** tab

-  **Response Signal**

-  **Plot** check box in list view

-  **Plot**: User can see the signal data on the opened scope dialog.

Iteration
^^^^^^^^^

Before the **Iteration** simulation of the **TSG**, the **FRF** simulation should be needed. Because, the Iteration simulation uses **inverse FRF** function.

The first drive signal :math:`{{\mathbf{A}}_{1}}(t)` is computed following <Check>equation (1).

.. math:: \begin{aligned}   & \mathbf{T}(t)\xrightarrow{FFT}\mathbf{T}(s) \\    & \mathbf{T}(s){{\mathbf{F}}^{-1}}(s)={{\mathbf{A}}_{1}}(s) \\    & {{\mathbf{A}}_{1}}(s)\xrightarrow[FF{{T}^{-1}}]{}{{\mathbf{A}}_{1}}(t) \\    \end{aligned}
   :label: 20_tsg_eq009


Where, :math:`\mathbf{T}(t)` and :math:`{{\mathbf{F}}^{-1}}(s)` are the target signals on the time domain and **inverse FRF** function, respectively.

.. figure:: media/image033.png
   :name: 20_tsg_image033

   First simulation of the **Iteration** simulation

The first simulation with the first drive signals. Then error signals
(:math:`{{\mathbf{E}}_{1}}(t)`) of the first simulation can be computed with following <Check>equation (2).

.. math:: {{\mathbf{E}}_{1}}(t)\equiv \mathbf{T}(t)-{{\mathbf{S}}_{1}}(t)
   :label: 20_tsg_eq012


The drive signal :math:`{{\mathbf{A}}_{2}}(t)` of the second simulation is computed following <Check>equation (3).

.. math:: \begin{aligned}   & {{\mathbf{E}}_{1}}(t)\xrightarrow{FFT}{{\mathbf{E}}_{1}}(s) \\    & {{\mathbf{A}}_{2}}(s)={{\mathbf{A}}_{1}}(s)+{{f}_{learning}}{{\mathbf{E}}_{1}}(s){{\mathbf{F}}^{-1}}(s) \\    & {{\mathbf{A}}_{2}}(s)\xrightarrow[FF{{T}^{-1}}]{}{{\mathbf{A}}_{2}}(t) \\    \end{aligned}
   :label: 20_tsg_eq014


Where, :math:`{{f}_{learning}}` is a scalar value and called a learning factor. The learning factor cannot be 0.0.

.. figure:: media/image034.png
   :name: 20_tsg_image034

   Second simulation of the **Iteration** simulation

After second simulation, we can compute the second error signals :math:`{{\mathbf{E}}_{2}}(t)`
again.

.. math:: {{\mathbf{E}}_{2}}(t)\equiv \mathbf{T}(t)-{{\mathbf{S}}_{2}}(t)
   :label: 20_tsg_eq017


In the case of the other simulation step, the second simulation procedure is repeated.

.. figure:: media/image035.png
   :name: 20_tsg_image035

   **Iteration** icon of the **Simulation** group in the **TSG** tab

.. figure:: media/image036.png
   :name: 20_tsg_image036

   **Iteration** dialog box

-  **FRF File (\*.FRF)**: Defines “\*.FRF” file by clicking **…**.

-  **FPLT**: Checks the **FRF** and the **inverse FRF** functions in the plot window.

-  **Use First Drive Signal (\*.TAI)**: Default is unchecked. If this is checked, then the first drive signal is replaced the user selected signals in the input “\*.TAI” file instead of <Check>equation (1).

-  **TAI File**: If the **Use First Drive Signal (\*.TAI)** is checked, then a “\*.TAI” file should be set using “…” file. The “\*.TAI” file can be generated **Export** function in `FRF Result <#TAI_Export_FRF>`__ and `Result <#TAI_Export_Result>`__
   dialogs.

-  **Plot**: If a “\*.TAI” file is selected, then User can see the signal data on the opened scope dialog.

-  **Cutoff Frequency**: In order to ignore data of the **inverse FRF**
   this option is needed. Data of **inverse FRF** is between the **Lower Bound** and the **Upper Bound** frequencies is used to compute the next **Drive Signal**.

-  **Lower Bound (Hz)**: Default is 0.0 Hz.

-  **Upper Bound (Hz)**: Default is 1000000.0 Hz

-  **Windowing Parameter for Drive Signals**: If the check box is selected, then a windowing function will be considered. Linear trapezoidal function is always computed.

-  **Data Size**: A natural value greater than 0 should be set. And the **Data Size** should be lower than the number of signal data.

-  **Linear/Step5** : Two interpolation function types are available for windowing function.

-  **Time Length** (s): A real number greater than 0.0 should be set.

   .. figure:: media/image019.png
      :name: 20_tsg_image019_1

      **Windowing function** for the **Iteration** simulation

.. figure:: media/image020.png
   :name: 20_tsg_image020_1

   Comparison of the interpolation types for **Windowing function**

-  **Iteration Parameters**

-  **Iteration Number**: The simulation is repeated with the **Iteration Number**. Default is 1.

-  **Learning Factor**: User can modify the learning factor :math:`{{f}_{learning}}` of <Check>equation (3). Default is 0.5. The range of the **Learning Factor**: :math:`0.0<{{f}_{learning}}\le 1.0`.

-  **TSG Result File (\*.TSG)**: Defines the output “\*.TSG” file saved all signal data.

-  **Analysis Setting**: **Dynamic/Kinematic Analysis** dialog is opened. Because, currently **TSG** is only supported dynamic/kinematic analysis. The **End Time** and **Step** should be match on **TSG** setting.

-  **End Time** data on the **Dynamic/Kinematic Anlaysis** dialog should be the same with the `End Time <#EndTime_Target>`__ of “\*.TARGET”
   data.

-  **Step** data on the **Dynamic/Kinematic Anlaysis** dialog should be set with (End_Time \* Sampling_Frequency).

   .. figure:: media/image029.png
      :name: 20_tsg_image029_1

      **Dynamic/Kinematic Analysis** dialog box

-  **Simulation**: The **Iteration** simulation is started.

Usage the Iteration simulation of TSG

.. image:: media/image036.png

#. Set “\*.FRF” file.

#. Set the Iteration Number.

#. Set the output “\*.TSG” file name and path.

#. Click **Analysis Setting**.

#. Set the **End Time** on the **Dynamic/Kinematic Analysis** dialog.
   The **End Time** should be set the same value of the “\*.TARGET”
   data.

#. Set the **STEP** on the **Dynamic/Kinematic Analysis** dialog. The **Step** should be the same with (**End_Time** \*
   **Sampling_Frequency**).

#. Click **OK** on the **Dynamic/Kinematic Analysis** dialog to leave.

#. Click **Simulate**.

Result
~~~~~~

You can check the result of the **Iteration** simulation of the **TSG**.

.. figure:: media/image037.png
   :name: 20_tsg_image037

   **Result** icon of the **Result** group in the **TSG** tab

.. figure:: media/image038.png
   :name: 20_tsg_image038

   **Result** dialog box

-  **TSG File (\*.TSG)**: Selects “\*.TSG” result file by clicking ….

-  **Error Rate**

-  **Plot**: User can check the following four **Error Rate** on each **Iteration Number**.

   The error for any sensor *i* at time *t* can be defined as:

   .. math:: {{e}_{i}}\left( t \right)={{T}_{i}}\left( t \right)-{{S}_{i}}\left( t \right)
      :label: 20_tsg_eq019


   Where, :math:`{{S}_{i}}(t)`: The signal of sensor *i* at time *t*. :math:`{{T}_{i}}(t)`: The target signal for sensor *i* at time *t*.

   The average signal :math:`{{S}_{i,average}}` and average target signal :math:`{{T}_{i,average}}` for any sensor *i* can be defined as :

..

   .. math:: {{S}_{i,average}}=\sum\limits_{d=1}^{nData}{\frac{{{S}_{i}}({{t}_{d}})}{nData}}
      :label: 20_tsg_eq024


   .. math:: {{T}_{i,average}}=\sum\limits_{d=1}^{nData}{\frac{{{T}_{i}}({{t}_{d}})}{nData}}
      :label: 20_tsg_eq025


Where, :math:`nData`: The number of data for each sensor (=End time x Sampling frequency + 1).

The root mean square signal :math:`{{S}_{i,RMS}}`, target signal :math:`<math></math>`, and error rate
:math:`{{e}_{i,RMS,rate}}` for any sensor *i* can be defined as:

   .. math:: {{S}_{i,RMS}}=\sqrt{\sum\limits_{d=1}^{nData}{\frac{{{({{S}_{i}}({{t}_{d}})-{{S}_{i,average}})}^{2}}}{nData}}}
      :label: 20_tsg_eq030


   .. math:: {{T}_{i,RMS}}=\sqrt{\sum\limits_{d=1}^{nData}{\frac{{{({{T}_{i}}({{t}_{d}})-{{T}_{i,average}})}^{2}}}{nData}}}
      :label: 20_tsg_eq031


   .. math:: {{e}_{i,RMS,rate}}=\left| \frac{{{S}_{i,RMS}}-{{T}_{i,RMS}}}{{{T}_{i,RMS}}} \right|
      :label: 20_tsg_eq032


From this, the following error terms can be derived:

.. list-table:: caption here
   :widths: 50 50
   :header-rows: 0


   * - Error Term
     - Equation

   * - **RMS**
     - :math:`\sqrt{\frac{\sum\limits_{i=1}^{nSensors}{\sum\limits_{d=1}^{nData}{e_{i}^{2}({{t}_{d}})}}}{n}}`

   * - **Max**
     - max(:math:`\left| {{e}_{i}}({{t}_{d}}) \right|`) for any :math:`i\in \{1,\ldots ,nSensors\}` and :math:`d\in \{1,\ldots ,nData\}`

   * - **Min**
     - min(:math:`\left| {{e}_{i}}({{t}_{d}}) \right|`) for any :math:`i\in \{1,\ldots ,nSensors\}` and :math:`d\in \{1,\ldots ,nData\}`

   * - **Average**
     - :math:`\frac{\sum\limits_{i=1}^{nSensors}{\sum\limits_{d=1}^{nData}{e_{i}^{{}}({{t}_{d}})}}}{n}`

   * - **RMS ErrorRate**
     - :math:`\sum\limits_{i=1}^{nSensors}{\frac{{{e}_{i,RMS,rate}}}{nSensors}}`


<Check>Table 1 Error Rate

Where, :math:`n`: The total number of data for all sensors (= Number of sensors x (End time x Sampling Frequency + 1) ).

-  **Iteration Number**: User can select the **Iteration Number**.

-  **Drive Signal**

-  **Plot** check box in list view

-  **Export**: User can make a “\*.TAI” or “\*.CSV” file including the drive signals.

-  **Plot**: User can see the signal data on the opened scope dialog.

-  **Response Signal**

-  **Plot** check box in list view

-  **Include Target Signal**: If this check box is checked, then the Target signals is added in the plot.

-  **Include Error Signal**: If this check box is checked, then the error signals (=Target(t) – Sensor(t)) is added in the plot.

-  **Plot**: User can see the signal data on the opened scope dialog.

.. |image1| image:: media/image009.png
.. |image2| image:: media/image015.png
