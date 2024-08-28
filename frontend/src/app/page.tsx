"use client";
import Image from "next/image";
import { useState } from "react";

import axios from "axios";



export default function Home() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const sendQuery = async () => {

    console.log(query);


    const options = {
      method: 'POST',
      url: 'http://localhost:5000/ask',
      params: { query: query },
      headers: { 'User-Agent': 'insomnia/8.6.0' }
    };

    try {

      const res = await axios.request(options)

      console.log(res.data);
      setResponse(res.data);
    } catch (error) {
      console.error(error);
    }


  }
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">

        <div className="fixed bottom-0 left-0 flex h-48 w-full items-end justify-center bg-gradient-to-t from-white via-white dark:from-black dark:via-black lg:static lg:size-auto lg:bg-none">
          <a
            className="pointer-events-none flex place-items-center gap-2 p-8 lg:pointer-events-auto lg:p-0"
            href="https://vercel.com?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app"
            target="_blank"
            rel="noopener noreferrer"
          >
            By{" "}
            <Image
              src="/vercel.svg"
              alt="Vercel Logo"
              className="dark:invert"
              width={100}
              height={24}
              priority
            />
          </a>
        </div>
      </div>

      {/* Logo  */}

      {/* AI Response */}
      {response && <div className="border-dark-3 mb-11 flex items-center rounded-md border border-l-[8px] border-l-[#1d4ed8] bg-dark-2 p-5 pl-8" >
        <div className="flex w-full items-center justify-between">
          <div>
            <h3 className="mb-1 text-lg font-medium text-white">
              {query}
            </h3>
            <p className="text-body-color dark:text-dark-6 text-sm">
              {response}
            </p>
          </div>

        </div>
      </div>
      }
      {/* Text Input section */}
      <div className="m-6 mb-32 flex relative w-full text-center">
        <input value={query} onChange={e => setQuery(e.target.value)} type="text" className="block w-full p-4 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="What do you know about John Brown from MIT?" required />
        <button onClick={sendQuery} className="text-white absolute end-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-8 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Ask</button>
      </div>

    </main>
  );
}
