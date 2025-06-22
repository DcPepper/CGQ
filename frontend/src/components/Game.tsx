import { Box, Button } from "@mui/material";
import { useLoaderData } from "react-router";
import Chart from "./Chart";

interface geoInterface {
    get_main_fields: string;
    get_filter_fields: string;
    area: 12189;
    capital: string;
    continent: string;
    flag: string;
    langue: string;
    lat: number;
    long: number;
    name: string;
    population: number;
    shape: string
}

export default function Game() {
    const res = useLoaderData() as geoInterface[];
    console.log(res)
    if (!res || res.length == 0) return <>loading</>
    let get_main_fields: string[] = JSON.parse(res[0].get_main_fields.replaceAll("'", "\""));
    console.log(get_main_fields)
    return (
        <>
        <Box sx={{display: 'flex', flexDirection: "column"}}>
        {get_main_fields.map(field => {
            return <Button id={`field-${field}`}>{field}</Button>
        })}
        </Box>
        <Chart>

        </Chart>
        </>
    )
}