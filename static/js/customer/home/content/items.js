

export function queryItems(limit, offset, filter){
    fetch(`/items/query/${limit}/${offset}/${filter}`)
        .then(r => r.json())
        .then(d => {
            console.log(d)
        })
}