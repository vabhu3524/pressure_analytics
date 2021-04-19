import pressure from './pressure.json';
import PressureChart from "./PressureChart";
import PressureStats from "./PressureStats";

function App() {

  return (
    <div className="App">

      {
        <div>
          <PressureChart data={pressure.pressure_data} />

          <PressureStats num_contractions={pressure.count_contractions}
            contraction_per_sec={pressure.contraction_per_sec}
          />
        </div>

      }
    </div>
  );
}

export default App;
