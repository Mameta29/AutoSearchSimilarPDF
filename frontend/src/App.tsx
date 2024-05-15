// src/App.tsx
import React, { useState } from 'react';
import { ChakraProvider, Box, Grid, Heading, useColorModeValue } from '@chakra-ui/react';
import SelectDataComponent from './components/SelectDataComponent';
import SearchComponent from './components/SearchComponent';

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const bgColor = useColorModeValue('gray.100', 'gray.700');

  return (
    <ChakraProvider>
      <Box padding={8} minHeight="100vh" bg={bgColor}>
        <Heading as="h1" size="xl" marginBottom={8} textAlign="center">
          類似ファイル検索
        </Heading>
        <Grid templateColumns="repeat(2, 1fr)" gap={12}>
          <SelectDataComponent onFileChange={setSelectedFile} />
          <SearchComponent selectedFile={selectedFile} />
        </Grid>
      </Box>
    </ChakraProvider>
  );
}

export default App;