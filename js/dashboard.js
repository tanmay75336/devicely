document.addEventListener("DOMContentLoaded", async () => {

  const { data: { user } } = await supabase.auth.getUser();

  if (!user) {
    window.location.href = "login.html";
    return;
  }

  const { data, error } = await supabase
    .from("previews")
    .select("*")
    .eq("user_id", user.id)
    .order("created_at", { ascending: false });

  if (error) {
    console.log(error);
    return;
  }

  const container = document.getElementById("cards-container");
  container.innerHTML = "";

  if (!data.length) return;

  data.forEach(item => {
    const div = document.createElement("div");
    div.className = "bg-white p-4 rounded-xl shadow";
    div.innerHTML = `
      <p class="font-semibold">${item.url}</p>
      <p class="text-xs text-gray-400">${new Date(item.created_at).toLocaleString()}</p>
    `;
    container.appendChild(div);
  });

});