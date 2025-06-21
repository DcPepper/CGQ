
import './App.css'
import Map from './components/Map';

import 'leaflet/dist/leaflet.css';
import { MapContainer, GeoJSON, TileLayer } from 'react-leaflet';
function App() {
  return (
    <>
      <Map />
      {/*<Legend/>*/}
    </>
  )
}

export default App
