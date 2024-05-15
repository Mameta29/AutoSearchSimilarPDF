// src/components/SearchComponent.tsx
import React, { useState } from 'react';
import { Box, Button, Grid, Heading, Image, Text, VStack, useToast } from '@chakra-ui/react';
import { FiSearch } from 'react-icons/fi';
import axios from 'axios';

interface SearchComponentProps {
  selectedFile: File | null;
}

function SearchComponent({ selectedFile }: SearchComponentProps) {
  const [similarDocuments, setSimilarDocuments] = useState<any[]>([]);
  const toast = useToast();

  const handleSearch = async () => {
    console.log('Selected file:', selectedFile)
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);
      console.log('Selected file:', selectedFile);
      console.log('FormData:', formData)

      try {
        const response = await axios.post('http://localhost:8000/search', formData);
        setSimilarDocuments(response.data);
        toast({
          title: 'Success',
          description: 'Similar documents found.',
          status: 'success',
          duration: 3000,
          isClosable: true,
        });
      } catch (error) {
        console.error('Error searching similar documents:', error);
        toast({
          title: 'Error',
          description: 'Failed to search similar documents.',
          status: 'error',
          duration: 3000,
          isClosable: true,
        });
      }
    }
  };

  return (
    <VStack spacing={6} alignItems="stretch">
      <Box borderWidth={1} borderRadius="md" padding={6} bg="white" boxShadow="md">
        <Heading as="h2" size="lg" marginBottom={4}>
          類似のファイルを検索
        </Heading>
        <Button onClick={handleSearch} variant="solid" colorScheme="blue" leftIcon={<FiSearch />} width="100%" height="60px">
          Search
        </Button>
      </Box>
      {similarDocuments.length > 0 && (
        <Box borderWidth={1} borderRadius="md" padding={6} bg="white" boxShadow="md">
          <Heading as="h3" size="md" marginBottom={4}>
            Similar Drawings
          </Heading>
          <Grid templateColumns="repeat(3, 1fr)" gap={6}>
            {similarDocuments.map((doc, index) => (
              <Box key={index} borderWidth={1} borderRadius="md" padding={4} bg="gray.100">
                <Image src={`http://localhost:8000/documents/${doc.document_id}.pdf`} alt={`Similar Document ${index + 1}`} marginBottom={2} />
                <Text fontSize="sm" textAlign="center">
                  Similarity: {doc.similarity_score.toFixed(2)}
                </Text>
              </Box>
            ))}
          </Grid>
        </Box>
      )}
    </VStack>
  );
}

export default SearchComponent;