
import { AppBar, Box, Typography } from '@mui/material'
import { Outlet } from 'react-router'
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';

const theme = createTheme({
  palette: {
    primary: {
      main: '#e4f1fe',
      dark: '#8dc6ff',
    },
    secondary: {
      main: '#22313f',
      dark: '#34495e',

    },
  },
});

function Header() {
  return (

      <Box>
        <header style={{
          borderBottom: "1px solid white",
          padding: 2,
          marginBottom: "1rem"
        }}>
          <Typography>Home</Typography>
        </header>
        <Outlet/>
      </Box>
  )
}

export default Header
