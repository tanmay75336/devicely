const supabase = window.supabaseClient;

document.addEventListener("DOMContentLoaded", async () => {

  const { data: { user } } = await supabase.auth.getUser();

  if (!user) {
    window.location.href = "login.html";
    return;
  }

  const urlParams = new URLSearchParams(window.location.search);
  const url = urlParams.get("url");

  if (url) {
    await savePreview(url, user.id);
  }

});

async function savePreview(url, userId) {
  await supabase.from("previews").insert([
    {
      user_id: userId,
      url: url
    }
  ]);
}