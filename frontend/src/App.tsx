import { useNavigate } from 'react-router-dom';
import './App.css'
import { Button } from './components/ui/button'
import AccountData from './components/AccountData';


function App() {
  const nav = useNavigate();
  return (
    <div className="bg-yellow-300 h-screen" >
            <div>
                </div>
                <Button onClick={() => nav('/Item')}> Go to Item</Button>
                <AccountData/>
                <div>

                </div>

    </div>
  )
}

export default App
