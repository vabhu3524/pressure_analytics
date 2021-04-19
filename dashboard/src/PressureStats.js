import React from 'react';

const PressureStats = ({ num_contractions, contraction_per_sec }) => {

    console.log(num_contractions + contraction_per_sec);
    return (
        <div>
          <h4>Count of contractions: {num_contractions}</h4>
          <h4>Contractions per seconds: {contraction_per_sec}</h4>
        </div>
    );
}

export default PressureStats;