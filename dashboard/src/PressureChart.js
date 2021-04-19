import React from 'react';
import ReactSignalsPlot from 'react-signals-plot';
const series = {
    data: [
        {
            id: 'Pressure Chart',
            values: [
                // {x:10,y:10},
                // {x:12,y:20},
                // {x:13,y:40},
                // {x:16,y:50}
            ]
        }
    ],
    labels: {
        x: 'X, ms',
        y: 'Y, kPa'
    }
};
const PressureChart = ({ data }) => {
    console.log(data);
    var dataPressure = data;
    for (let index = 0; index < dataPressure.length; index++) {
        series.data[0].values.push({ x: dataPressure[index].ms, y: dataPressure[index].pressure });
    }

    return (
        <div>
            <ReactSignalsPlot
                style={{ width: '100%', height: 450 }}
                data={series.data}
                samplesLimit={2000}
                labels={series.labels}
                interactive={true}
            />
        </div>
    );
}

export default PressureChart;