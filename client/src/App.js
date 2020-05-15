import React, { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'
import './App.css'
import Button from 'react-bootstrap/Button'
import Jumbotron from 'react-bootstrap/Jumbotron'
import Container from 'react-bootstrap/Container'
import Spinner from 'react-bootstrap/Spinner'

export default function App() {
    const [title, setTitle] = useState('')
    const [synopsis, setSynopsis] = useState('')
    const [isLoading, setIsLoading] = useState(false)

    const getPrediction = async () => {
        setIsLoading(true)
        const { title, synopsis } = await fetch('/predict').then(response => response.json())
        setTitle(title)
        setSynopsis(synopsis)
        setIsLoading(false)
    }

    return (
        <Container className="main">
            <h2 style={{ marginBottom: '1.5rem', fontSize: '3rem' }}>Generate Anime Titles and Synopses</h2>
            {title || synopsis ? (
                <Jumbotron>
                    {title && <h3 style={{ marginBottom: '1rem' }}>{title}</h3>}
                    {synopsis && <p>{synopsis}</p>}
                </Jumbotron>
            ) : null}
            <Button onClick={getPrediction} disabled={isLoading}>{isLoading ? (
                <Spinner animation="border" role="status">
                    <span className="sr-only">Loading...</span>
                </Spinner>
            ) : `Generate ${title || synopsis ? 'another' : ''} response`}</Button>
        </Container>
    )
}
