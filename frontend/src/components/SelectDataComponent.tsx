// src/components/SelectDataComponent.tsx
import React, { useState } from 'react';
import { Box, Button, Heading, Image, VStack } from '@chakra-ui/react';
import { FiUpload } from 'react-icons/fi';
import { Document, Page, pdfjs } from 'react-pdf';

pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/${pdfjs.version}/pdf.worker.js`;

interface SelectDataComponentProps {
  onFileChange: (file: File | null) => void;
}

function SelectDataComponent({ onFileChange }: SelectDataComponentProps) {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0] || null;
    setSelectedFile(file);
    onFileChange(file);
  };

  return (
    <VStack spacing={6} alignItems="stretch">
      <Box borderWidth={1} borderRadius="md" padding={6} bg="white" boxShadow="md">
        <Heading as="h2" size="lg" marginBottom={4}>
          PDFを選択
        </Heading>
        <Button
          as="label"
          htmlFor="file-input"
          variant="outline"
          colorScheme="blue"
          leftIcon={<FiUpload />}
          width="100%"
          height="200px"
          borderStyle="dashed"
          cursor="pointer"
        >
          Choose PDF file
          <input id="file-input" type="file" accept=".pdf" style={{ display: 'none' }} onChange={handleFileChange} />
        </Button>
      </Box>
      {selectedFile && (
        <Box borderWidth={1} borderRadius="md" padding={6} bg="white" boxShadow="md" maxHeight="400px" overflow="auto">
          <Heading as="h3" size="md" marginBottom={4}>
            選択されたPDF
          </Heading>
          {/* <Image src={URL.createObjectURL(selectedFile)} alt="Selected PDF" /> */}
          <Document file={selectedFile} onLoadError={console.error}>
            <Page pageNumber={1} width={400}/>
          </Document>
        </Box>
      )}
    </VStack>
  );
}

export default SelectDataComponent;