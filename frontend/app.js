const searchButton=document.querySelector('.search-button');
searchButton.addEventListener('click',()=>{
    const searchInput=document.querySelector('#search');
    const query=searchInput.value.trim();
    if(query==''){
        alert('Please enter a search query');
        return;
    }
    fetchSearchResults(query);
})
async function fetchSearchResults(query){
    try{
        const response=await fetch(`http://127.0.0.1:8000/search?q=${encodeURIComponent(query)}&top_k=5`);
        // if(!response.ok){
        //     throw new Error('Network response was not ok');
        // }
        const data=await response.json();
        console.log('Search results:',data);
        displaySearchResults(data.results);
    }    catch(error){
        console.error('Error fetching search results:',error);
        alert('An error occurred while fetching search results. Please try again later.');
    }   
}function displaySearchResults(results){
    const resultsContainer=document.querySelector('.results-container');
    resultsContainer.innerHTML='';
    if(results.length===0){
        resultsContainer.innerHTML='<p>No results found.</p>';
        return;
    }
    results.forEach(result=>{
        const resultElement=document.createElement('div');
        resultElement.classList.add('result-item');
        resultElement.innerHTML=`
            <a href="${result.url}" target="_blank">
                <h3>${result.title}</h3>
                <img src="${result.img_url}" alt="${result.title}" class="result-image">
            </a>
        `;
        resultsContainer.appendChild(resultElement);
    });
}