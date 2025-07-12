import ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router";
import './App.css'

import Header from "../src/Header"
import Home from "./components/Home";
import Game from "./components/Game";
import React from "react";

let router = createBrowserRouter([
  {
    path: "/",
    element: <Header />,
    children: [
      {
        index: true,
        element: <Home />
      },
      {
        path: "game/:q",
        element: <React.Suspense fallback={<>wait</>}><Game /></React.Suspense>,
        loader: async (params) => {
          console.log(params)
          let res = await fetch(`http://localhost:8000/api/${params.params.q}/`);
          return res
        }
      }
    ]
  },
]);

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <RouterProvider router={router} />
);
