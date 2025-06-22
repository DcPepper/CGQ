import { Box, Card } from "@mui/material";
import { Link, NavLink } from "react-router";

export default function Home() {
    const THEMES = [
        {name: "Geography", url: "geo"},
        {name: "Japonais", url: "jap"},
    ]
    return (
        <Card sx={{backgroundColor: "#8dc6ff", padding: "1rem", display: "flex", flexDirection: "column", gap: 2}}>
            {THEMES.map(theme => {
                return (
                    <NavLink to={`game/${theme.url}`} key={`theme-${theme.url}`} style={{
                        all: "unset",
                        cursor: "pointer", 
                        border: "1px solid white",
                        padding: ".5rem",
                        }}>
                        {theme.name}
                    </NavLink>
                )
            })}
        </Card>
    )
}