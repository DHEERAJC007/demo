import './App.css';
import Batches from './Components/Batches';
import Calendars from './Components/Calendars';
import Dues from './Components/Dues';
import QeBatchTabs from './Components/QeBatchTabs';
import QcBatchTabs from './Components/QcBatchTabs';
import Visualization from './Components/Visulization';

function App() {
  return (
    <div className="App">
      <div className="part1">
        <Batches />
        <Calendars />
      </div>
      <div className="part2">
        <Dues />
        <Visualization />
      </div>
      <div className="part3">
        <QeBatchTabs />
        <QcBatchTabs />
      </div>
    </div>
  );
}

export default App;
