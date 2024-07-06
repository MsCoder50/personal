import express from 'express';
import cors from 'cors';
import pool from './db.js';
import multer from 'multer';
import { join, extname } from 'path';
import { unlinkSync, existsSync } from 'fs';

const app = express();
const port = 4000;

app.use(cors());
app.use(express.json());

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    const __dirname = new URL('.', import.meta.url).pathname;
    cb(null, join(__dirname, "../public/img/"));
  },
  filename: function (req, file, cb) {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    const fileExt = extname(file.originalname);
    cb(null, `${uniqueSuffix}${fileExt}`);
  }
});

const upload = multer({ storage });

app.post('/create', upload.single('image'), async (req, res) => {
  const { uid, title, content, category } = req.body;
  let image = req.file.filename;
  image = "/img/" + image;
  try {
    const [result] = await pool.query(
      'INSERT INTO Blog (UID, title, content, category, image) VALUES (?, ?, ?, ?, ?)',
      [uid, title, content, category, image]
    );

    res.status(201).json({ message: 'Blog created successfully', blogId: result.insertId });
  } catch (error) {
    console.error('Error creating blog:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

app.post('/Signup', async (req, res) => {
  const { email, username, password } = req.body;

  try {
    const [emailCheck] = await pool.query('SELECT COUNT(*) AS count FROM User WHERE email = ?', [email]);
    if (emailCheck[0].count > 0) {
      return res.status(400).json({ error: 'Email already exists' });
    }

    const [usernameCheck] = await pool.query('SELECT COUNT(*) AS count FROM User WHERE username = ?', [username]);
    if (usernameCheck[0].count > 0) {
      return res.status(400).json({ error: 'Username already exists' });
    }

    const [result] = await pool.query(
      'INSERT INTO User (email, username, password) VALUES (?, ?, ?)',
      [email, username, password]
    );

    const uid = result.insertId;

    res.status(201).json({ message: 'User created successfully', UID: uid });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Server error' });
  }
});

app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  try {
    const [rows] = await pool.query('SELECT UID, email, password FROM User WHERE email = ? AND password = ?', [email, password]);
    if (rows.length > 0) {
      res.status(200).json({ UID: rows[0].UID });
    } else {
      res.status(401).json({ error: 'Invalid email or password' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Server error' });
  }
});

app.get('/Blog', async (req, res) => {
  const image = req.query.image;

  try {
    let query;
    let params;

    if (image) {
      query = 'SELECT * FROM Blog WHERE Image = ?';
      params = [image];
    } else {
      query = 'SELECT * FROM Blog';
      params = [];
    }

    const [rows] = await pool.query(query, params);
    if (image && rows.length === 0) {
      return res.status(404).json({ error: 'Blog not found' });
    }
    res.status(200).json(image ? rows[0] : rows);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Server error' });
  }
});

app.get('/Blogs/:uid', async (req, res) => {
  const { uid } = req.params;

  try {
    const [rows] = await pool.query('SELECT * FROM Blog WHERE UID = ?', [uid]);
    res.status(200).json(rows);
  } catch (error) {
    console.error('Error fetching blogs:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

app.post('/deleteBlog', async (req, res) => {
  const { imgname } = req.body;

  const imagePathToDelete = join(__dirname, "../public", imgname);
  if (existsSync(imagePathToDelete)) {
    unlinkSync(imagePathToDelete);
  }

  try {
    const [result] = await pool.query('DELETE FROM Blog WHERE Image = ?', [imgname]);

    res.status(200).json({ message: 'Blog and image deleted successfully' });
  } catch (error) {
    console.error('Error deleting blog:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

app.get('/fetchBlog/:image', async (req, res) => {
  const { image } = req.params;
  try {
    const [rows] = await pool.query('SELECT * FROM Blog WHERE Image = ?', [image]);
    res.status(200).json(rows);
  } catch (error) {
    console.error('Error fetching blog:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

app.post('/editBlog', upload.single('image'), async (req, res) => {
  const { imagePath, title, content, category } = req.body;
  let newImage = req.file ? req.file.filename : null;
  newImage = newImage ? "/img/" + newImage : null;

  try {
    if (newImage) {
      const oldImagePath = imagePath
      if (existsSync(oldImagePath)) {
        unlinkSync(oldImagePath);
      }

      const [result] = await pool.query(
        'UPDATE Blog SET title = ?, content = ?, category = ?, image = ? WHERE Image = ?',
        [title, content, category, newImage, imagePath]
      );

      if (result.affectedRows === 0) {
        return res.status(404).json({ error: 'Blog not found' });
      }
    } else {
      const [result] = await pool.query(
        'UPDATE Blog SET title = ?, content = ?, category = ? WHERE Image = ?',
        [title, content, category, imagePath]
      );

      if (result.affectedRows === 0) {
        return res.status(404).json({ error: 'Blog not found' });
      }
    }

    res.status(200).json({ message: 'Blog updated successfully' });
  } catch (error) {
    console.error('Error updating blog:', error);
    res.status(500).json({ error: 'Server error' });
  }
});

app.listen(port, () => {
  console.log(`App listening on port ${port}`);
});
